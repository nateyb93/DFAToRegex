import state;
import pprint;

class dfa(object):
    """A valid DFA has:\n\t1. accept state(s)\n\t2. transitions from each symbol\n\t3. no empty transitions"""
    def __init__(self, states = [], alphabet = [], transitions = [], acceptStates = []):
        self.states = states;
        self.alphabet = alphabet;
        self.startState = state.dfaState("q1", True, False);
        self.states.append(self.startState);
        self.acceptStates = acceptStates;


    def addToAlphabet(self, symbol):
        """Adds a symbol to the alphabet for the DFA"""
        if(symbol not in self.alphabet):
            self.alphabet.append(symbol);
            print("Symbol '" + symbol + "' added.");
        else:
            print(symbol + "is already in the alphabet for this DFA.");

        self.prettyPrint();

    def removeFromAlphabet(self, symbol):
        """removes a symbol from the DFA alphabet"""
        if symbol not in self.alphabet:
            self.alphabet.append(symbol);
    
    def getState(self, name):
        """gets a state with the specified name or returns None"""
        for dfaState in self.states:
            if name == dfaState.name:
                return dfaState;
                
        return None;

    def addState(self, name):
        """Adds a state to the DFA"""
        newState = state.dfaState(name, False, False);

        "check if state is already in alphabet"
        if self.getState(name) != None:
            print("State '" + name + "' already in alphabet.");
            return;
        

        self.states.append(newState);
        print("State '" + name + "' added.");
        self.prettyPrint();
        return;
        

    def removeState(self, name):
        """Removes a state from the DFA"""
        stateToRemove = None;

        for state in self.states:
            if name == state.name:
                stateToRemove = state;

        if(stateToRemove != None):
            self.states.remove(stateToRemove);
            print("State '" + name + "' removed.\n");
        else:
            print("No state to remove!\n");

        self.prettyPrint();

    def printTransitions(self):
        """prints the transition table for the DFA"""
        print("\u03B4 = ");
        print("\t", end = "");

        "print '0th' label row"
        for state in self.states:
            print(state.name + "\t", end = "");

        print();

        "print rows"
        for rowState in self.states:
            print(rowState.name + "\t", end = "");

            "print a column for each row"
            for columnState in self.states:
                toTransition = rowState.getTransition(columnState);
                if toTransition != None:
                    print(toTransition.symbol + "\t", end = "");
                else:
                    print("\t", end = "");
            print();"newline"

        print();

    
    def prettyPrint(self):
        """Prints the formal description for the DFA."""

        print("\nThe current properties of your DFA are...");

        "set of states"
        print("         Q = [", end = "");
        for state in self.states:
            print("'" + state.name + "', ", end = "");
        print("]");

        "symbol alphabet"
        print("         \u03A3 = ", end = ""), pprint.pprint(self.alphabet);
        
        "transition table"
        print("         \u03B4 = (see below)");

        "start state"
        print("    Qstart = " + self.startState.name);

        "accept states"
        print("Qaccept(s) = ", end = ""), pprint.pprint(self.acceptStates);

        print();
        self.printTransitions();
        print();

    def validate(self):
        """Validates that the DFA is in valid form"""
        for state in self.states:
            for transitions in state.transitions:
                "do stuff"