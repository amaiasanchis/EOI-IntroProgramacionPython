import requests
u = {'Nombre':'Billy','Apellidos':'Vanegas'}
# anadimos info con post
r=requests.post('http://postman-echo.com/post',data=u)
print(r.text)
