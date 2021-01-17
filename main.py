from AutoCompleteData import *


# note : treat errors


def main():
    auto_complete_tree = Node("")
    curr_root = auto_complete_tree
    with open("our_text.txt", 'r') as file:
        line = file.readline()
        while line != '':  # The EOF char is an empty string
            # set the tree for 1 sentence
            if line[-1] == '\n':
                line = line[:-1]
            for i in range(len(line)):
                for char in line[i:-1]:
                    curr_root = curr_root.add_child(char)
                curr_root = curr_root.add_child(line[-1], line)
                curr_root = auto_complete_tree
            line = file.readline()

    #
    # print("auto_complete_tree\n " , auto_complete_tree)
    #
    # print("leaves: ", auto_complete_tree.children["i"].get_leaves())
    print("get_all_completions: ", get_all_completions("ea", auto_complete_tree))


if __name__ == '__main__':
    main()
