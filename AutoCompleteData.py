from dataclasses import dataclass
from tree_node import Node

@dataclass
class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
    
    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score
    
    def get_offset(self):
        return self.offset

    def __str__(self):
        return self.completed_sentence + self.source_text.__str__()
  




def get_all_completions(txt, root: Node):
    if txt == "":
        return root.get_leaves()
    if root.children:
       
        if txt[0].isalnum() or (txt[0] == ' ' and (len(txt)==1 or (len(txt)>1 and txt[1] !=' '))):   
            cur_node = root.children.get(txt[0].lower())    
        else:
            cur_node = root
             
        if cur_node:
            return get_all_completions(txt[1:], cur_node)

    return []

