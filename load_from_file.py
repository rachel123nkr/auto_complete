import pickle

from AutoCompleteData import get_all_completions

with open('auto_complete_tree.obj', 'rb') as fp:
    banana = pickle.load(fp)

print(banana)
print("get_all_completions: ", get_all_completions("is", banana))
