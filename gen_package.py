import os
from os import walk

def load_classes():
    if os.path.isdir('src/classes'):
        files = []
        for (dirpath, dirnames, filenames) in walk('src/classes'):
            files.extend(filenames)
            break
        for f in files:
            if not f.endswith('.cls'):
                files.remove(f);
    return files;

def load(path):
    if os.path.isdir(path):
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
            break
        for f in files:
            if not f.endswith('.cls'):
                files.remove(f);
    return files;

# verify src folder exists
if not os.path.isdir('src'):
    quit(0)

# open file
text_file = open("src/package.xml", "w")
# write headers
text_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
text_file.write('<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n')
# write classes
classes = load('src/classes')
print classes
if len(classes) > 0:
    text_file.write('\t<types>\n')
    for c in classes:
        text_file.write('\t\t<members>'+c[:-4]+'</members>\n')
    text_file.write('\t\t<name>ApexClass</name>\n')
    text_file.write('\t</types>\n')

# close package
text_file.write('\t<version>39.0</version>\n')
text_file.write('</Package>\n')

text_file.close()


#text_file.write("Purchase Amount: %s" % TotalAmount)
