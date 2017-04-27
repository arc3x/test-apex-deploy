import os
from os import walk

def load(path, ext):
    if os.path.isdir(path):
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
            break
        for f in files:
            if (not f.endswith(ext)) || f.endswith('.meta'):
                files.remove(f);            

    return files;

def write_xml(file_in, name_in, list_in):
    if len(list_in) == 0:
        return 0
    file_in.write('\t<types>\n')
    for l in list_in:
        file_in.write('\t\t<members>'+os.path.splitext(os.path.basename(l))[0]+'</members>\n')
    file_in.write('\t\t<name>'+name_in+'</name>\n')
    file_in.write('\t</types>\n')

# verify src folder exists
if not os.path.isdir('src'):
    quit(0)

# open file
text_file = open("src/package.xml", "w")
# write headers
text_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
text_file.write('<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n')
# write classes
classes = load('src/classes', '.cls')
write_xml(text_file, 'ApexClass', classes)
print classes
triggers = load('src/triggers', '.trigger')
write_xml(text_file, 'ApexTrigger', triggers)

# close package
text_file.write('\t<version>39.0</version>\n')
text_file.write('</Package>\n')

text_file.close()


#text_file.write("Purchase Amount: %s" % TotalAmount)
