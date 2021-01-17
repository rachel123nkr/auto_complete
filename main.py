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
            for char in line:
                curr_root = curr_root.add_child(char.lower())
            line = file.readline()
            curr_root = auto_complete_tree

    # print("auto_complete_tree\n " , auto_complete_tree)

    # print("leaves\n " , auto_complete_tree.children["g"].get_leaves())
    print("get_all_completions", get_all_completions("i eat", auto_complete_tree))


if __name__ == '__main__':
    main()
