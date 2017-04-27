import os
from os import walk

# returns a list of all files in path who have extention ext
def load(path, ext):
    if os.path.isdir(path):
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            files.extend(filenames)
            break
        out = []
        for f in files:
            if f.endswith(ext):
                out.append(f)
    return out;

# writes a name_in xml block to file_in iterating over values from list_in
def write_xml(file_in, name_in, list_in):
    if len(list_in) == 0:
        return 0
    file_in.write('\t<types>\n')
    for l in list_in:
        file_in.write('\t\t<members>'+os.path.splitext(os.path.basename(l))[0]+'</members>\n')
    file_in.write('\t\t<name>'+name_in+'</name>\n')
    file_in.write('\t</types>\n')



###
# main
###

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
print 'classes ' + classes
# write triggers
triggers = load('src/triggers', '.trigger')
write_xml(text_file, 'ApexTrigger', triggers)
print 'triggers ' + triggers
#write pages
pages = load('src/pages', '.page')
write_xml(text_file, 'ApexPage', pages)
print 'pages ' + pages
# close package
text_file.write('\t<version>39.0</version>\n')
text_file.write('</Package>\n')
# done
text_file.close()
