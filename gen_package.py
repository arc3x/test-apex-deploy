#import zipfile
import shutil
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

# zips a directory and moves the resulting resource file into a staticresources folder in the dest directory
def zip_to_static_resource(dir_to_zip, zip_name, dest):
    # verify file structure
    if not os.path.isdir(dir_to_zip):
        return 0
    if not os.path.isdir(dest):
        return 0
    if dest.endswith('/'):
        dest = dest[:-1]
    # build full path
    full_dest_path = dest + '/staticresources'
    # creat staticresources folder if not existant
    if os.path.isdir(dest) and not os.path.isdir(full_dest_path):
        os.makedirs(full_dest_path)
    # zip dir
    # zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)
    # for root, dirs, files in os.walk(dir_to_zip):
    #     for file in files:
    #         zipf.write(os.path.join(root, file))
    # zipf.close()
    shutil.make_archive(zip_name, 'zip', dir_to_zip)
    shutil.move(zip_name+'.zip', full_dest_path+'/'+zip_name+'.resource')



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
print 'classes ' + str(classes)
# write triggers
triggers = load('src/triggers', '.trigger')
write_xml(text_file, 'ApexTrigger', triggers)
print 'triggers ' + str(triggers)
#write pages
pages = load('src/pages', '.page')
write_xml(text_file, 'ApexPage', pages)
print 'pages ' + str(pages)
# build & write static resource
zip_to_static_resource('app', 'app', 'src')
resources = load('src/staticresources', '.resource')
write_xml(text_file, 'StaticResource', resources)
print 'resources ' + str(resources)
# close package
text_file.write('\t<version>39.0</version>\n')
text_file.write('</Package>\n')
# done
text_file.close()
