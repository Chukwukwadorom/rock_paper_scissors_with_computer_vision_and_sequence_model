import os
from housekeeping import rps_base_dir
import xml.etree.ElementTree as ET

### here is to check if there is any unlabeled or wrongly labeled image

base_dir = f"{rps_base_dir}/rough_work"



rock_folder = os.path.join(base_dir, "rock")
paper_folder = os.path.join(base_dir, "paper")
scissors_folder = os.path.join(base_dir, "scissors")

rock_xml_folder = os.path.join(base_dir, "full_rock_label_xml")
paper_xml_folder = os.path.join(base_dir, "full_paper_label_xml")
scissors_xml_folder = os.path.join(base_dir, "full_scissors_label_xml")

os.chdir(base_dir)

folder_dict = {rock_folder: rock_xml_folder, paper_folder: paper_xml_folder,scissors_folder: scissors_xml_folder}

for img_folder, xml_folder in folder_dict.items():

    xml_files = os.listdir(xml_folder)
    os.chdir(xml_folder)
    for xml_file in xml_files:
        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()
        foldername = root.findall('folder')[0].text
        filename = root.findall('filename')[0].text
        pathname = root.findall('path')[0]
        pathname.text = f"/{foldername}/{filename}"

        tree.write(xml_file)

    os.chdir("../")










