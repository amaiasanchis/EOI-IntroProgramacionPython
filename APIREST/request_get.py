import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
print(r.text)
print(r.json()['iss_position']['longitude'])
print(r.json()['iss_position']['latitude'])