import json
import json

merged = {}

with open('users1.json') as firstFile:
    data1 = json.load(firstFile)
    merged.update(data1['table']['users'])

with open('users2.json') as secondFile:
    data2 = json.load(secondFile)
    merged.update(data2['table']['users'])

merged_list = list(merged.values())

with open('users.json', 'w') as f:
    json.dump(merged_list, f, indent=4)