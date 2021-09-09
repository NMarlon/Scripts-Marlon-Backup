

import sys
import json
import requests
import pycurl
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

"""
sudo pip install python-pipedrive
sudo pip install pycurl
sudo pip install 

"""


"""
test="kkkj"
 test.lower()
 test.upper()
test.title()#"abc abc" -> "Abc Abc"
 test.swapcase()# Todas maiusculas





string = "Há muito tempo!"

new_string = ''.join(char for char in string if char.isalnum())
print(new_string)


import re

new_string = re.sub(r"[^a-zA-Z0-9]","",string)
print(new_string)


from unidecode import unidecode

str1 = 'café'
print(unidecode(str1))
 
"""


# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/python-pipedrive-master/pipedrive/')
sys.path.insert(1, '/python-pipedrive-master/')

#import file
from  pipedrive  import  Pipedrive 
pipedrive  =  Pipedrive ( "b5fb60012c9a4fd703ffc5623f3b027d32b3042e" ) 
pipedrive.organizations(method='GET')


print(dir(pipedrive))
print("")
print(vars(pipedrive))
print("")

def responde(content):
	print("code:")
	print(vars(content))
	print("")
	print("")
valor="valor"
res = requests.get('https://api.pipedrive.com/v1/organizations/find?api_token=b5fb60012c9a4fd703ffc5623f3b027d32b3042e&term='+valor)
#responde(res)

#responde(curl('https://api.pipedrive.com/v1/organizations/find?api_token=b5fb60012c9a4fd703ffc5623f3b027d32b3042e&term=microsoft'))

#POSTAR ALGUEM

print(pipedrive.organizations(method='GET'))
"""
pipedrive.deals({
            'title': 'Big Risen',
            'value': 1000000,
            'org_id': 2045,
            'status': 'open'
        }, method='POST')
"""
  #pipedrive.activities({'id': 6789}, method='DELETE')
#print(vars(pipedrive.http))



"""
#ENCONTRAR ALGUEM
term="name"
response = pipedrive.persons_find({'term':term}, method='GET')
results = response['data']
suggestions = ["Big"]
if results != None:
        for result in results:
            suggestions.append({'value': result['name'], 'data': result})
json_response = {'query': term, 'suggestions': suggestions}
data = json.dumps(json_response)

print("")
print("AQUi:")
print(json_response)
"""
#Codigo extraído de: python-pipedrive 
#Link: https://github.com/jscott1989/python-pipedrive/blob/master