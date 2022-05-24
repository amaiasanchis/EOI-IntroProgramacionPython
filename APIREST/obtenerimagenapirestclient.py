import requests
url = 'https://www.python.org/images/success/nasa.jpg'
#no sabemos si responde por get o por post, pero 
# probamos por get porque es el que se usa en el navegador

#get tiene parametros. con el paramentro stream avisamos a get
# de que puede obtener una informacion bastante amplia
r= requests.get(url, stream=True)

#quiero dejar en data la respuesta a get
#creo el archivo de descarga para escribir y en binario por ser una imagen
with open('./imagen_download.jpg','wb') as file:
    #vamos guardando por trozos (por si es muy grande, 
    #para evitar problemas de que no se guarde todo)
    for trozo in r.iter_content():
        file.write(trozo)

r.close()