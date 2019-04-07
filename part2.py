# Python 3.6.3 Scripting Examples by Rich K for Task 29842
# Note a lot of this is similar in Python 2, but not the same
# Remember, Ctrl+Z then Enter to exit a command line python session in Windows

# Copy Files
import sys, os, shutil
print ("*************Copy Files*************")
copyFile = sys.argv[0]
destFile = os.path.dirname(sys.argv[0]) + '\copy_' + os.path.basename(sys.argv[0])
print(f"{destFile}")
print (f"Copying {copyFile} to {destFile}")
shutil.copy2(sys.argv[0], destFile) # target filename is /dst/dir/file.ext
print ("Copy finished!")

# Write XML
print ("*************Write XML*************")
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="foo").text = "bar"
tree = ET.ElementTree(root)
xmlFile = os.path.dirname(sys.argv[0]) + '\example.xml'
tree.write(xmlFile)

# Read XML
print ("*************Read XML*************")
tree = ET.parse(xmlFile)  
print("Value of foo is: ", tree.getroot()[0][0].text)

# Delete File
print ("*************Delete File*************")
print(f"Deleting {xmlFile}...")
os.remove(xmlFile)
print(f"Deleted...")


