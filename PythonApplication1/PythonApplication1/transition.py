class dfaTransition(object):
    """transition defines a transition on a symbol between two DFA states"""

    def __init__(self, endState, symbol):
        self.endState = endState;
        self.symbol = symbol;

