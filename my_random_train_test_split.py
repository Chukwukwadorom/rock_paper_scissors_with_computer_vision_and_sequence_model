

import os
import numpy as np
from housekeeping import rps_base_dir
import random
import shutil



base_dir = os.path.join(rps_base_dir, "house_keeping_updated")

rock_folder = os.path.join(base_dir, "rock")
paper_folder = os.path.join(base_dir, "paper")
scissors_folder = os.path.join(base_dir, "scissors")


rock_xml_folder =os.path.join(base_dir, "full_rock_label_xml")
paper_xml_folder =os.path.join(base_dir, "full_paper_label_xml")
scissors_xml_folder =os.path.join(base_dir, "full_scissors_label_xml")

 
train = os.path.join(base_dir, "train")
test = os.path.join(base_dir, "test")

# some useful functions

def randomise_files(folder, train_prop=0.7):
  files_names = os.listdir(folder)
  random.shuffle(files_names)
  thresh = int(np.ceil(len(files_names) * 0.7))
  train_files = files_names[:thresh]
  test_files = files_names[thresh:]

  return train_files, test_files



def copy_files(train_files, test_files, folder_name):
  """
  this function copies files to train and test folders
  :param train_files:
  :param test_files:
  :param folder_name:
  :return:
  """
  if not os.path.exists(train):
    os.mkdir(train)
  if not os.path.exists(test):
    os.mkdir(test)

  def replace_extension(file_name):
    file_name = list(file_name)
    file_name[-4:]=".xml"
    return "".join(file_name)

  train_files_xml =  list(map(replace_extension, train_files))
  test_files_xml =  list(map(replace_extension, test_files))
  
  if folder_name == "rock":
    # copying train data set
    for file_name in train_files:
      shutil.copy(os.path.join(rock_folder,file_name), train)
    for file_name in train_files_xml:
      shutil.copy(os.path.join(rock_xml_folder,file_name), train)

    # copying test data set
    for file_name in test_files:
      shutil.copy(os.path.join(rock_folder,file_name), test)
    for file_name in test_files_xml:
      shutil.copy(os.path.join(rock_xml_folder,file_name), test)

  elif folder_name == "paper":
    # copying train data set
    for file_name in train_files:
      shutil.copy(os.path.join(paper_folder,file_name), train)
    for file_name in train_files_xml:
      shutil.copy(os.path.join(paper_xml_folder,file_name), train)

    # copying test data set
    for file_name in test_files:
      shutil.copy(os.path.join(paper_folder,file_name), test)
    for file_name in test_files_xml:
      shutil.copy(os.path.join(paper_xml_folder,file_name), test)

  elif folder_name == "scissors":
    # copying train data set
    for file_name in train_files:
      shutil.copy(os.path.join(scissors_folder,file_name), train)
    for file_name in train_files_xml:
      shutil.copy(os.path.join(scissors_xml_folder,file_name), train)

    # copying test data set
    for file_name in test_files:
      shutil.copy(os.path.join(scissors_folder,file_name), test)
    for file_name in test_files_xml:
      shutil.copy(os.path.join(scissors_xml_folder,file_name), test)

  else:
    pass

os.chdir(base_dir)

folder_dict = {rock_folder:"rock", paper_folder: "paper",scissors_folder: "scissors"}

for folder in folder_dict:
  train_files, test_files = randomise_files(folder, train_prop=0.7)
  copy_files(train_files, test_files, folder_dict[folder])

train_len = len(os.listdir(train))//2
test_len = len(os.listdir(test))//2

print(f"train len: {train_len}")
print(f"test len: {test_len}")

print(f"total len: {test_len + train_len}")

print(f"every image : {len(os.listdir(os.path.join(base_dir, 'every_img')))}")
print(f"every xml : {len(os.listdir(os.path.join(base_dir, 'every_xml')))}")

