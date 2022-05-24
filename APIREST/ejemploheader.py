import requests
import json

url='http://httpbin.org/post' #endpoint de conexion
user= json.dumps({'Username':'Billy'}) #dumps para serializar a str el contenido del json
header= {'content-type':'application/json'}
r = requests.post(url,data=user,headers=header)
print(r.text)

'''
{
  "args": {}, 
  "data": "{\"Username\": \"Billy\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "21",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.27.1",
    "X-Amzn-Trace-Id": "Root=1-628ca8d1-201ced39155c2b0833c485bc"  },
  "json": {
    "Username": "Billy"
  },
  "origin": "84.232.45.18",
  "url": "http://httpbin.org/post"
}
'''