import transition;

class dfaState(object):
    """state defines a state object within a dfa. states have a name, and two booleans that define whether the state is the start state or an accept state"""

    def __init__(self, name, isStart, isAccept, transitions = []):
        self.name = name;
        self.isStart = isStart;
        self.isAccept = isAccept;
        self.transitions = transitions;


    def addTransition(self, endStateName, symbol):
        """adds a transition to the state"""
        myTransition = object();
        for aTransition in self.transitions:
            if symbol == aTransition.symbol:
                return False;

        myTransition = transition.dfaTransition(endStateName, symbol);
        return True;

    def removeTransition(self, symbol):
        """removes the transition on the specified symbol from the state"""
        for aTransition in self.transitions:
            if symbol == aTransition.symbol:
                self.transitions.remove(aTransition);
                return True;

        return False;