import json
import sys
from SwoPyApi.SwoPy import getHomeworkHTML
from SwoPyApi.parser import parser


if __name__ == "__main__":

    try:
        auth = open("../auth/auth.json", "r")
        options = json.loads(auth.read())
        auth.close()
    except:
        print("auth.json not found")
        sys.stderr.write("ERR::COULD NOT FIND HOMEWORK DIV -> PLEASE UPDATE AUTH.JSON\n")
        sys.exit("Programm failed to retrive data")

    html = getHomeworkHTML(options) # Get inner html from swop
    p = parser(html) # create parser instance

    print(p.getString())

    

    





