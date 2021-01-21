import pickle


def save_tree(auto_complete_tree):
    with open('auto_complete_tree.obj', 'wb') as fp:
        pickle.dump(auto_complete_tree, fp)


def load_tree():
    print("Loading the files....")
    with open('auto_complete_tree.obj', 'rb') as f:
        return pickle.load(f)
