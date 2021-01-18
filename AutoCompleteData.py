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
        self.complete_senteces = []
        self.children = dict()


    def add_child(self, char, line = None):
        if char == ',':
            char = ' '
        if self.prefix != '' and self.prefix[-1] == ' ' and char == ' ':
            return self
        if not self.children.get(char.lower()):    
            self.children[char.lower()] = Node(self.prefix + char)
        if line:
            self.children[char.lower()].complete_senteces.append(line)

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

        
      
            


def get_all_completions(txt, root: Node):
    if txt == "":
        return root.get_leaves()
    if root.children:
       
        if txt[0] == ' ' and  len(txt)>1 and txt[1] ==' ':   
            cur_node = root                                                      
        elif txt[0] == ',' or txt[0] == ' ':
            cur_node = root.children.get(' ')
        else:
            cur_node = root.children.get(txt[0].lower())
       
        if cur_node:
            return get_all_completions(txt[1:], cur_node)
        


        # if txt[0] != ',' or txt[0] != ' ' or (txt[0] == ' ' and  len(txt)>1 and txt[1]!=' ') :
        #     cur_node = root.children.get(txt[0].lower())
        #     if cur_node:
        #         return get_all_completions(txt[1:], cur_node)
        # else:
        #      return get_all_completions(txt[1:], root)

        # else:
        #     if txt[0] == ' ':
        #         cur_node = root.children.get(',')
        #     if txt[0] == ',':
        #         cur_node = root.children.get(' ')
        #     if cur_node:
        #         return get_all_completions(txt[1:], cur_node)
        #     if txt[0] in [',', ' ']:
        #         return get_all_completions(txt[1:], root)


    return []

