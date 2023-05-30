import os
from housekeeping import rps_base_dir
import xml.etree.ElementTree as ET

### here is to check if there is any unlabeled or wrongly labeled image

base_dir = f"{rps_base_dir}/every_xml"
os.chdir(base_dir)
empty_count = 0
empty_xml =[]
xml_files = os.listdir(base_dir)

for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    obj = root.findall('object')[0]
    name = obj.find('name').text
    if name not in ["rock", "paper", "scissors"]:
        empty_count +=1
        empty_xml.append(xml_file)


print(empty_count)
print(empty_xml)




