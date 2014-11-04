class dfa(object):
    """dfa defines a dfa object with all the elements of the 5 tuple"""
    states;
    alphabet;
    transitions;
    startState;
    acceptStates;

    def __init__(self, states = [], alphabet = [], transitions = [], startState = None, acceptState = []):
        self.states = states;
        self.alphabet = alphabet;
        self.transitions = transitions
        self.startState = startState;
        self.acceptState = acceptState;

    
    def addState(self, state):
        states.append(state);
        "add transition information"
        for transition in state.transitions:
            self.transitions.append(transition);