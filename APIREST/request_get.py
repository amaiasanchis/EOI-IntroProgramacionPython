import requests

# hacemos una llamada con get
r = requests.get('http://api.open-notify.org/iss-now.json')
# sacamos por pantalla el texto de la respuesta
print(r.text)
# {"timestamp": 1653427856, "iss_position": {"latitude": "-39.4520", "longitude": "-153.9285"}, "message": "success"}
# seleccionamos el valor de longitud y latitud (dicc dentro de json)
print(r.json()['iss_position']['longitude'])
print(r.json()['iss_position']['latitude'])

