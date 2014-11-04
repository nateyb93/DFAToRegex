class state(object):
    """state defines a state object within a dfa. states have a name, and two booleans that define whether the state is the start state or an accept state"""
    name;
    isStart;
    isAccept;
    transitions;

    def __init__(self, name, isStart, isAccept, transitions = []):
        self.name = name;
        self.isStart = isStart;
        self.isAccept = isAccept;
        self.transitions = transitions;


