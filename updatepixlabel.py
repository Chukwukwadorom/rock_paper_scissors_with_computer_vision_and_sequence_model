import os
import time

### get list of pictures in directory
### get list of labels
### compare them
### remove labeled pictures from pix directory


base_dir = "/Users/Kwado/Desktop/labeling"
pictures = f"{base_dir}/continue_labeling"
anot = f"{base_dir}/present_anot"

os.chdir(base_dir)

# print(os.listdir(pictures))
# print(set(list(map(lambda x:x[-4:], os.listdir(pictures)))))



##getting list of pictures in directory

def get_list(dir):
    """ returns a list of string representing images/ anot.
     the list will be stripped of its extention to enable comparison"""
    list_str = os.listdir(dir)
    return list(map(lambda x: x[:-4], list_str))



def compare_str(anot_strs, pix_strs):
    to_be_deleted = []
    for str in anot_strs:
        if str in pix_strs:
            to_be_deleted.append(str)

    return to_be_deleted


def delete_pix(to_be_deleted, dir):
    dir_items = os.listdir(dir)
    for file in to_be_deleted:
        png = f"{file}.png"
        jpg = f"{file}.jpg"
        if png in dir_items:
            os.remove(os.path.join(dir, png))
        elif jpg in dir_items:
            os.remove(os.path.join(dir, jpg))
        else:
            pass


if __name__ == "__main__":
    pix_strs = get_list(pictures)
    anot_strs = get_list(anot)
    print(len(pix_strs))
    print(len(anot_strs))
    to_be_deleted = compare_str(anot_strs, pix_strs)
    delete_pix(to_be_deleted, pictures)
    print(len(os.listdir(pictures)))
    print(len(anot_strs))



#
time.sleep(5)

