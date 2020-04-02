from dfa import *


def main():
    while True:
        dfa = Dfa('dfa.json')

        user_input = input('Input string: ')
        print(dfa.run(list(user_input)))


if __name__ == "__main__":
    main()
