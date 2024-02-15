import json
x = '{ "firstName": "tester", "lastName": "tester", "city": "Vilnius"}'
y = json.loads(x)
y["firstName"] = "MANTAS"
y["lastName"] = "LAPP"
y["age"] = "24"
print(y["firstName"], y["lastName"], y["city"], y["age"])