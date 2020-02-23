class Dfa:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def transition_to_state(self, input_value):
        if (self.initial_state, input_value) not in self.transitions.keys():
            self.initial_state = None
            return
        self.initial_state = self.transitions[(self.initial_state, input_value)]
        return

    def in_accept_state(self):
        return self.initial_state in self.accepting_states

    def run(self, input_list):
        for inp in input_list:
            self.transition_to_state(inp)
        return self.in_accept_state()
