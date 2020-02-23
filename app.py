from dfa import *
import json


def main():
    states, alphabet, transitions, initial_state, accepting_states = parse_file()

    while True:
        dfa = Dfa(states, alphabet, transitions, initial_state, accepting_states)

        user_input = input('Input string: ')

        print(dfa.run(list(user_input)))


def parse_file():
    with open('functions.json', 'r') as f:
        dfa_dict = json.load(f)

    dfa_dict = dfa_dict[0]
    states = dfa_dict['states']
    alphabet = dfa_dict['alphabet']
    transitions = parse_transitions(dfa_dict['transitions'])
    initial_state = dfa_dict['initial_state']
    accepting_states = dfa_dict['accepting_states']

    return states, alphabet, transitions, initial_state, accepting_states


def parse_transitions(transitions_to_parse):
    transitions = dict()
    for transition in transitions_to_parse:
        transitions[(transition[0], transition[1])] = transition[2]
    return transitions


if __name__ == "__main__":
    main()
