from dataclasses import dataclass
from tree_node_class import *

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
  


