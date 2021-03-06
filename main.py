from handle_score import *
from save_and_load_on_file import load_tree


def online():
    loaded_tree = load_tree()

    while True:
        text = input("The system is ready, please enter your text:\n")
        sentence = ''
        while text != '#':
            sentence += text
            top_5_sentences = get_top_5_sentences(sentence, loaded_tree)
            print_sentences(top_5_sentences)
            text = input(sentence)


def main():
    online()


if __name__ == '__main__':
    main()
