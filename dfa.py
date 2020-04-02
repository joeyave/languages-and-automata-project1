import json


class Dfa:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            dfa_dict = json.load(f)

        self.alphabet = dfa_dict['alphabet']
        self.transitions = {}
        for transition in dfa_dict['transitions']:
            self.transitions[(transition[0], transition[1])] = transition[2]
        self.initial_state = dfa_dict['initial_state']
        self.accepting_states = dfa_dict['accepting_states']

    def transition_to_state(self, input_value):
        if (self.initial_state, input_value) not in self.transitions.keys():
            if input_value not in self.alphabet:
                print("wrong symbol")
            self.initial_state = None
        else:
            prev_state = self.initial_state
            self.initial_state = self.transitions[(self.initial_state, input_value)]
            print(f"{prev_state} -> {self.initial_state}")

    def in_accept_state(self):
        return self.initial_state in self.accepting_states

    def run(self, input_list):
        for inp in input_list:
            print(f"{inp}: ", end="")
            self.transition_to_state(inp)
        return self.in_accept_state()
