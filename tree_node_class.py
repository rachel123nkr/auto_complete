class Node(object):
    def __init__(self, current_char):
        self.current_char = current_char
        self.complete_senteces = []
        self.children = dict()

    def add_child(self, char, line_data=None):
        if self.current_char == ' ' and char == ' ':
            return self
        if not self.children.get(char.lower()):
            self.children[char.lower()] = Node(char)
        if line_data:
            self.children[char.lower()].complete_senteces.append(line_data)

        return self.children[char.lower()]

    def get_leaves(self):
        list_res = []
        self.get_leaves_recursive(list_res)
        return list_res

    def get_leaves_recursive(self, lst):
        for sentence in self.complete_senteces:
            lst.append(sentence)

        if self.children:
            for v in self.children.values():
                v.get_leaves_recursive(lst)


def get_all_completions(txt, root: Node):
    if txt == "":
        return root.get_leaves()
    if root.children:

        if txt[0].isalnum() or (txt[0] == ' ' and (len(txt) == 1 or (len(txt) > 1 and txt[1] != ' '))):
            cur_node = root.children.get(txt[0].lower())
        else:
            cur_node = root

        if cur_node:
            return get_all_completions(txt[1:], cur_node)

    return []
