from AutoCompleteData import *
import json
import os
import pickle

from datetime import datetime


# note : treat errors

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
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time strart =", current_time)

    path_list = get_path_list('python-3.8.4-docs-text')

    auto_complete_tree = Node("")
    curr_root = auto_complete_tree

    # path_list = ['our_text.txt']
    for path in path_list:
        print(path)
        with open(path, 'r') as file:
            line = file.readline()
            line_counter = 0
            while line != '':  # The EOF char is an empty string
                # set the tree for 1 sentence
                if line != '\n':
                    if line[-1] == '\n':
                        line = line[:-1]
                    # striped_line = "".join(ch for ch in line if str(ch).isalnum() or ch == " ")
                    for i in range(len(line)):
                        for char in line[i:-1]:
                            if str(char).isalnum() or char == " ":
                                curr_root = curr_root.add_child(char)
                            else:
                                continue
                        curr_root = curr_root.add_child(line[-1], AutoCompleteData(line, (path, line_counter), i, None))
                        curr_root = auto_complete_tree
                line = file.readline()
                line_counter += 1

    print("ennnndddddd")

    current_time = now.strftime("%H:%M:%S")
    print("Current Time end =", current_time)
    # print("auto_complete_tree\n " , auto_complete_tree)
    # print("leaves: ", auto_complete_tree.children["b"].get_leaves())
    with open('auto_complete_tree.obj', 'wb') as fp:
        pickle.dump(auto_complete_tree, fp)

    print("get_all_completions: ", [(obj.completed_sentence, obj.source_text,obj.offset)  for obj in get_all_completions("eat", auto_complete_tree)])


if __name__ == '__main__':
    main()
