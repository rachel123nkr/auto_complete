from AutoCompleteData import *
import json
import os

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

    path_list = [' ']
    for path in path_list:

        with open('our_text.txt', 'r') as file:
            line = file.readline()
            while line != '':  # The EOF char is an empty string
                # set the tree for 1 sentence
                if line != '\n':
                    if line[-1] == '\n':
                        line = line[:-1]
                    striped_line = "".join(ch for ch in line if ch is str(ch).isalnum())     
                    for i in range(len(striped_line)):
                        for char in striped_line[i:-1]:
                            curr_root = curr_root.add_child(char)
                        curr_root = curr_root.add_child(striped_line[-1], line)
                        curr_root = auto_complete_tree
                line = file.readline()

    print("ennnndddddd")
    
    current_time = now.strftime("%H:%M:%S")
    print("Current Time end =", current_time)    
        # print("auto_complete_tree\n " , auto_complete_tree)
        #print("leaves: ", auto_complete_tree.children["b"].get_leaves())
    print("get_all_completions: ", get_all_completions("i eat", auto_complete_tree))




if __name__ == '__main__':
    main()
