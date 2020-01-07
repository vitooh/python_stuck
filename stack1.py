import requests
import sys

r = requests.get("http://stackoverflow.com/questions/57908596")

print (r.text.find('<div id="answers">'))

