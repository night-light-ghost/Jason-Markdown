
import csv
import json

#markdown_table = """| Some Title | Some Description             | Some Number |
#|------------|------------------------------|-------------|
#| Dark Souls | This is a fun game           | 5           |
#| Bloodborne | This one is even better      | 2           |
#| Sekiro     | This one is also pretty good | 110101      |"""

# lines = markdown_table.split("\n")

def fileIntoObject(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    merriWeb = {}
    definition = ""

    for line in lines:
        if(line[0]=="#"):
            hashes=0
            while(line[hashes]=="#"):
                hashes++
            
            section = []
            
            merriWeb[line[hashes:]]=section
            while
            merriWeb[] = 

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


# Recursive function diving into lines list
# merriWeb needs to be a global variable to work here and above
def hashish(lines, lineIndex):
    #Parsing through the hashes, recursively
    if(lines[lineIndex][0]=="#"):
        hashes=0
        while(lines[lineIndex][hashes]=="#"):
            hashes++
        merriWeb[lines[lineIndex][hashes:]] = hashish(lines,lineIndex++)
    #Breaking down image urls
    elif(lines[linesIndex][0]=="!"):
        name = ""
        for char in lines[linesIndex][1:]:
            if(char!=']'):
                name = name+char
            else:
                break
        url = ""
        for char in lines[linesIndex][len(char)+4:]:
            if(char!=']'):
                url = url+char
            else:
                break
        merriWeb['image'] = {'name': name, 'url':url}
        lineIndex++
    #Breaking down urls
    elif(lines[linesIndex][0]=="["):
        text = ""
        for char in lines[linesIndex][0:]:
            if(char!=']'):
                tet = text+char
            else:
                break
        url = ""
        for char in lines[linesIndex][len(char)+3:]:
            if(char!=']'):
                url = url+char
            else:
                break
        merriWeb['link'] = {'text': text, 'url':url}
        lineIndex++
    cursor = lineIndex
    while(lines[lineIndex][0].notIn{'|','#','-'}):
        lineIndex++
    return = lines[cursor:lineIndex]


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
    

def parseHeader(lines, index):

# jsonDumps can tack the dictionary and lists within and print it as a json
# this will need to <F3>be done to a file for very end output
def printObjects():
        print(json.dumps(data, sort_keys=True, indent=4))

main(printObjects(fileIntoObject('temp-table.md'))
