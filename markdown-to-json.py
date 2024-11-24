
import csv
import json

#markdown_table = """| Some Title | Some Description             | Some Number |
#|------------|------------------------------|-------------|
#| Dark Souls | This is a fun game           | 5           |
#| Bloodborne | This one is even better      | 2           |
#| Sekiro     | This one is also pretty good | 110101      |"""

# lines = markdown_table.split("\n")

def fileIntoObject(cursor, fileName):
    with open('temp-table.md', 'r') as file:
        lines = file.readlines()
    index = 0
    merriWeb = {}
    syntax={
        '!':parseImage(lines, index),
        '[':parseLink(lines, index),
        '|':parseTable(lines, index),
        '#':parseHeader(lines, index),
        '-':parseBullet(lines, index),
        }
    while(lines[index]!=""):
        syntax.get(lines[index][0])


# Code expects a list of strings, each one being a line in the over-arching table
# Code returns a list of key, value pairs spliy into dictionaries by row
def parseTable(lines, index):
    dict_reader = csv.DictReader(lines, delimiter="|")
    data = []
    # skip first row, i.e. the row between the header and data
    for row in list(dict_reader)[1:]:
        # strip spaces and ignore first empty column
        r = {k.strip(): v.strip() for k, v in row.items() if k != ""}
        data.append(r)
    

# jsonDumps can tack the dictionary and lists within and print it as a json
# this will need to be done to a file for very end output
def printObjects():
        print(json.dumps(data, sort_keys=True, indent=4))
