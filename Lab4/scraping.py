import requests
from bs4 import BeautifulSoup
import json

req = requests.get('https://student.fizyka.pw.edu.pl/~pioleb/')

#print(req.status_code)
#print(req.text)
#print(req.request.headers)

soup = BeautifulSoup(req.text, 'html.parser')

dane = soup.find('table')
dane = dane.text

print(dane)

plik = "kot_dane.json"

with open('Lab4/'+plik, 'w') as f:
    json.dump(dane, f)
