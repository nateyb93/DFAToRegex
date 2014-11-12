import transition as dfaTransition;

class dfaState(object):
    """state defines a state object within a dfa. states have a name, and two booleans that define whether the state is the start state or an accept state"""

    def __init__(self, name, isStart, isAccept, transitions = []):
        self.name = name;
        self.isStart = isStart;
        self.isAccept = isAccept;
        self.transitions = transitions;

    def addTransition(self, end, symbol):
        """adds a transition to the state object"""
        for transition in self.transitions:
            if transition.symbol == symbol:
                print("State " + self.name + " already has a transition on symbol " + symbol);
                return;
        "if no transition was found on the specified symbol, add it."
        self.transitions.append(dfaTransition.dfaTransition(end, symbol));


    def removeTransition(self, symbol):
        """removes a transition from the state object"""
        for transition in self.transitions:
            if symbol == transition.symbol:
                self.transitions.remove(transition);


    def getTransition(self, symbol):
        """gets a transition from the state with the specified name"""
        for transition in self.transitions:
            if symbol == transition.symbol:
                return transition;

        return None;