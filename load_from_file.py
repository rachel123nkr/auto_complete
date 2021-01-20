import pickle

def load_tree():
    print("Loading the files....")
    with open('auto_complete_small_tree.obj', 'rb') as f:
        return pickle.load(f)