# Jason-Markdown

## Project work done in here

Thoughts of a basic markdown to code editor
It doesn't need to work for everything, it can just work for me as I am to interpret it
Will probably be a subset of Markdown file formates and types
You thought of the following:
    read in a file of markdown
    first pass, loop through line by line, creating array of lines
    for each line, there's gonna be a check for the starting caracter
        per character found, have a method to interpret the kind of object from the syntax
        keeping in mind the depth of headers as a baseline for which object fields are within each other, 
            write these objects to a json file line by line
            will need a few variable registers to keep track of depth
                Or like one big "cursor" object
                coordinates in a way
                just have a number with tens places? that might overcomplicate
                maybe a list of lists, and their lengths of elements increase or decrease as particularly needed
Do it for the ability to do this all backwards too

