import json
pesos_json= """{
    "json":True,
    {
        "nod_e":"0",#id nodo de saída
        "nod_s":"1",
        "peso":0.5
    },
    {
        "nod_e":"0",#id nodo de saída
        "nod_s":"2",
        "peso":0.5
    },
}"""


procura_por_json = json.loads(pesos_json)
if "json" in procura_por_json:
    print("Key exist in JSON data")
else:
    print("Key doesn't exist in JSON data")
