import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    # r= requests.get(url)
    # print(r.text) #contenido de la url
    '''
    {
    "cookies": {}
    }
    '''
    #para mandar cookies a traves de una peticion 
    cookies = {
        'my-cookie': 'true'
    } 
   
    response = requests.get(url, cookies=cookies)
    # print(response.text)
    '''
    {
    "cookies": {
        "my-cookie": "true"
    }
    }'''

    if response.status_code==200: # todo ok, sin error
        cookies = response.cookies #duda
        print(cookies) #<RequestsCookieJar[]>

        print("El contenido es:")
        print(response.content)