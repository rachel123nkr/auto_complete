class Node(object):
    def __init__(self, prefix):
        self.prefix = prefix  # sentance
        self.complete_senteces = []
        self.children = dict()


    def add_child(self, char, line_data = None):
        if self.prefix != '' and self.prefix[-1] == ' ' and char == ' ':
            return self
        if not self.children.get(char.lower()):
            self.children[char.lower()] = Node(self.prefix + char)
        if line_data:
            self.children[char.lower()].complete_senteces.append(line_data)

        return self.children[char.lower()]

    def __str__(self):
        res = self.prefix + "  children: \n"
        for k in self.children:
            res += self.children[k].__str__() + " "
        return res

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