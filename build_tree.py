from auto_complete_data_class import *
from tree_node_class import *
import os
from save_and_load_on_file import save_tree
from datetime import datetime


def print_now_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time start =", current_time)


def build_tree(file_path):
    print_now_time()

    path_list = get_path_list(file_path)

    auto_complete_tree = Node("")
    curr_root = auto_complete_tree

    for path in path_list:
        print(path)
        try:
            with open(path, 'r', encoding="utf8") as file:
                line = file.readline()
                line_counter = 1
                while line != '':
                    if line != '\n':
                        if line[-1] == '\n':
                            line = line[:-1]
                        line = line[0:200]
                        index = 0
                        while line[index] == ' ':
                            index += 1
                        for i in range(index, len(line)):
                            last_index = 1
                            for char in line[i:-1]:
                                if str(char).isalnum() or char == " ":
                                    curr_root = curr_root.add_child(char)
                                    last_index += 1
                                else:
                                    continue
                                if last_index == 17:
                                    break
                            curr_root = curr_root.add_child(line[-1],
                                                            AutoCompleteData(line, (path, line_counter), i, None))
                            curr_root = auto_complete_tree
                    line = file.readline()
                    line_counter += 1
        except:
            print("error: ", path)

    print_now_time()
    print("saving.....")

    save_tree(auto_complete_tree)

    print("end")
    print_now_time()


def get_path_list(startpath):
    path_list = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        middle_path = os.path.basename(root)
        all_path = startpath + '/'
        if level > 0:
            all_path += middle_path
            all_path += '/'
        for file_path in files:
            path_list.append(all_path + file_path)
    return path_list


def main():
    build_tree('Archive')


if __name__ == '__main__':
    main()
