import html_to_json
import json
import os

class Parser:

    def __init__(self, html):
        self.jsonhtml = html_to_json.convert(html)


    def getJson(self):
        return self.jsonhtml

    def getString(self):
        string = ""
        string += "\n=============================\n"

        for j, i in enumerate(self.jsonhtml['div']):
            assignment = i['div'][0]['div'][0]['b'][0]["_value"]
            teacher = i['div'][0]['i'][0]['_value'].replace('von ', '')
            subject = i['div'][0]['span'][0]['strong'][0]['_value']
            date = i['div'][0]['span'][1]['_value']
            deadline = i['div'][0]['span'][2]['_value']
            string += f"Aufgabe nummer {j + 1}\n"
            string += f"{assignment}\n von {teacher}\n Fach : {subject}\n Datum : {date} Abgabe : {deadline}\n"
            string += "=============================\n"
            print(date)
        print(string)
        return string

    def getArray(self):
        arr = []
        for j, i in enumerate(self.jsonhtml['div']):
            assignment = i['div'][0]['div'][0]['b'][0]["_value"]
            teacher = i['div'][0]['i'][0]['_value'].replace('von ', '')
            subject = i['div'][0]['span'][0]['strong'][0]['_value']
            arr.append([subject, teacher, assignment])
        return arr

    def saveJson(self):
        try:
            os.remove("../../homework.json")
        except:
            pass

        with open("./homework.json", "w") as json_file:
            json_file.write(json.dumps(self.jsonhtml, indent=4, sort_keys=True))



    