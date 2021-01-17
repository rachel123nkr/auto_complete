from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    # methods that you need to define by yourself


# def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
#     pass

class Node(object):
    def __init__(self, prefix):
        self.prefix = prefix  # sentance
        self.children = dict()

    def add_child(self, char):
        if not self.children.get(char):
            self.children[char] = Node(self.prefix + char)
        return self.children[char]

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
        if not self.children:
            lst.append(self.prefix)
        else:
            for v in self.children.values():
                v.get_leaves_recursive(lst)


def get_all_completions(txt, root: Node):
    if txt == "":
        return root.get_leaves()
    if root.children:
        cur_node = root.children.get(txt[0].lower())
        if cur_node:
            return get_all_completions(txt[1:], cur_node)
    return []

