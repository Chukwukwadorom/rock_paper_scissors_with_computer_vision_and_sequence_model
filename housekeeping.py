import os


rps_base_dir = "/Users/Kwado/Desktop/rps_ssd/house_keeping"
rocks_path = f"{rps_base_dir}/rock"
papers_path = f"{rps_base_dir}/paper"
scissors_path = f"{rps_base_dir}/scissors"

rocks_xml_path = f"{rps_base_dir}/full_rock_label_xml"
papers_xml_path = f"{rps_base_dir}/full_paper_label_xml"
scissors_xml_path = f"{rps_base_dir}/full_scissors_label_xml"
os.chdir(rps_base_dir)

rocks_list = os.listdir(rocks_path)
papers_list = os.listdir(papers_path)
scissors_list = os.listdir(scissors_path)

rocks_xml_list = os.listdir(rocks_xml_path)
papers_xml_list = os.listdir(papers_xml_path)
scissors_xml_list = os.listdir(scissors_xml_path)


list_path_ext = [{"list_str":rocks_list, "path":rocks_path, "ext":"rock"},
                 {"list_str":papers_list, "path":papers_path, "ext":"paper"},
                {"list_str":scissors_list, "path":scissors_path, "ext": "scissors"},

                {"list_str":rocks_xml_list, "path":rocks_xml_path, "ext":"rock"},
                 {"list_str":papers_xml_list, "path":papers_xml_path, "ext":"paper"},
                 {"list_str":scissors_xml_list, "path":scissors_xml_path, "ext":"scissors"}
                 ]


def add_suffix(rps_dict):
    """
    :param rps_dict: a dictionary containing list of files(list_str), path of the host directory(path),
     and name to be added to file name(ext)
    :return:
    """
    list_str = rps_dict.get("list_str")
    path = rps_dict.get("path")
    ext = rps_dict.get("ext")

    new_list_str = list(map(lambda x: f"{x[:-4]}_{ext}{x[-4:]}", list_str))

    for index_file in range(len(new_list_str)):
        try:
            ## compare bare file name stripped off extensions and recent addition
            assert list_str[index_file][:-4] == new_list_str[index_file][:-5-len(ext)], f"{list_str[index_file]}" \
                                                                                        f" and {new_list_str[index_file]} " \
                                                                                        f"are not the same file"
        except AssertionError as msg:
            print(msg)

        else:
            # os.rename(f"{path}/{list_str[index_file]}", f"{path}/{new_list_str[index_file]}")
            pass





for folder in list_path_ext:
    add_suffix(folder)