import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'

    response = requests.get(url)

    if response.status_code == 200:
        # print(response.content)
        # metemos el contenido de la respuesta en la variable content
        content = response.content
        #creamos un fichero y escribimos en este la info
        file = open('google.html','wb')
        file.write(content)
        file.close()