import html_to_json
import json
import os

html_file = open("./example.html", "r")
html = html_file.read()
html_file.close()

output = html_to_json.convert(html)

try:
    os.remove("./homework.json")
except:
    pass

'''
json_file = open("./homework.json", "w")

json_file.write(json.dumps(output, indent=4, sort_keys=True))

json_file.close()
'''

j = 1

print("\n")
print("================================")

for i in output['div'][0]['div']:
    assignment = i['div'][0]['div'][0]['b'][0]["_value"]
    teacher = i['div'][0]['i'][0]['_value'].replace('von ', '')
    subject = i['div'][0]['span'][0]['strong'][0]['_value']
    date = i['div'][0]['span'][1]['_value']
    deadline = i['div'][0]['span'][2]['_value']  
    print("Assignment number ", j)
    print("{}, \n by {} from your {} class, \n from {} till {}".format(assignment, teacher, subject, date, deadline))
    print("================================")
    j += 1



