from dfa import *
import json


def main():
    while True:
        dfa = Dfa()
        dfa.load_from_file('dfa.json')

        user_input = input('Input string: ')

        print(dfa.run(list(user_input)))


if __name__ == "__main__":
    main()
