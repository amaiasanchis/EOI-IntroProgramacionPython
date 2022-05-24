import requests
import json

#lo hacemos primero sin especificar parametros y nos da lo que aparece en l12-16
'''
version inicial

import requests
url = 'https://pokeapi.co/api/v2/pokemon-form'
r = requests.get(url)
print(r.text)
'''
# en el output vemos esto
# ? offset=20&limit=20
# esto son los parametros que se pasan (tras la ?)
#pokemon-form es el metodo
'''
"https://pokeapi.co/api/v2/pokemon-form?offset=20&limit=20"
'''

#queremos reproducir en python lo que nos da en el navegador

def get_pokemons(url, offset=0):
    #param = {'offset':40} 
    # dumps no hace falta, param se puede tomar directamente como diccionario
    # nos da como respuesta los pokemons del 20-40

    #damos a offset el valor de una variable para poder sacar la lista completa 
    param = {'offset':offset} 
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    r = requests.get(url, params=param)
    
    if r.status_code == 200: #comprobacion de que todo va bien, no hay error
        #la respuesta a requests la metemos en un json
        # esta contiene diversa info como la url, los nombres y urls de cada pokemon, etc.
        resultado = r.json()
        # print(resultado)

        #creamos una lista con los nombres y url de cada pokemon
        # 'results' es la clave de la entrada del diccionario resultado de la que queremos obtener info
        # get para obtener el valor del dicc: get(key,[]) ([] porque en este caso es una lista)
        lista_pokemons = resultado.get('results',[]) 
        # print(lista_pokemons)
        # obtenemos una lista en la que cada elemento es un diccionario con dos entradas
        # ej.: {'name': 'squirtle', 'url': 'https://pokeapi.co/api/v2/pokemon-form/7/'}

        if lista_pokemons: #comprobacion de que esta creada
            # recorremos la lista por cada elemento (diccionario)
            for pokemon in lista_pokemons:
                name = pokemon['name']
                print(name)
        # print(r.text)
        continuar = input('Desea seguir con mas pokemons?(y/n)').lower()

        if continuar == 'y':
            get_pokemons(url,offset+20) #iterativa


#llamamos a la funcion def get_pokemons
if __name__=='__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    get_pokemons(url) 

