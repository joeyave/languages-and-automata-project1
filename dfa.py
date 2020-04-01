import json


class Dfa:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = dict()
        self.initial_state = []
        self.accepting_states = []

    def load_from_file(self, file_name):
        with open(file_name, 'r') as f:
            dfa_dict = json.load(f)

        dfa_dict = dfa_dict[0]
        self.states = dfa_dict['states']
        self.alphabet = dfa_dict['alphabet']
        self.transitions = dfa_dict['transitions']
        self.initial_state = dfa_dict['initial_state']
        self.accepting_states = dfa_dict['accepting_states']

    def transition_to_state(self, input_value):
        if str((self.initial_state, input_value)) not in self.transitions.keys():
            if input_value not in self.alphabet:
                print("wrong symbol")
            self.initial_state = None
        else:
            prev_state = self.initial_state
            self.initial_state = self.transitions[str((self.initial_state, input_value))]
            print(f"{prev_state} -> {self.initial_state}")

    def in_accept_state(self):
        return self.initial_state in self.accepting_states

    def run(self, input_list):
        for inp in input_list:
            print(f"{inp}: ", end="")
            self.transition_to_state(inp)
        return self.in_accept_state()
