import requests
import pprint


r = requests.get("http://18.195.167.117:5000/validate/username?username=test_username")

r = requests.post(
    url='http://18.195.167.117:5000/signup',
    json={"username": "Wojtek_tester","password": "testowehaslo","firstname": "Wojtek","lastname": "TestoweNazwisko"}
)

pprint.pprint(r.json())