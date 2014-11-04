class transition(object):
    """transition defines a transition on a symbol between two DFA states"""
    startState;
    endState;
    symbol;

    def __init__(self, startState, endState, symbol):
        self.startState = startState;
        self.endState = endState;
        self.symbol = symbol;

