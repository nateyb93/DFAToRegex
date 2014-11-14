import pprint;
from collections import namedtuple;
from itertools import combinations;

class dfa(object):
    """A valid DFA has:\n\t1. accept state(s)\n\t2. transitions from each symbol\n\t3. no empty transitions"""
    transition = namedtuple("transition", "endState, symbol");

    def __init__(self, states = [], alphabet = [], acceptStates = []):
        self.states = states;
        self.alphabet = alphabet;
        self.transitionFunction = dict();
        self.startState = 'q0';
        self.states.append(self.startState);
        self.transitionFunction[self.startState] = [];
        self.acceptStates = acceptStates;
        

    def addState(self, state):
        """Adds a state to the DFA"""
        if state not in self.states:
            self.states.append(state);
            self.transitionFunction[state] = [];
            print ("State " + state + " added.\n");
            print();
            
        else:
            print("State " + state + " already in the alphabet.\n");
            print();

        self.printTuple();

    def removeState(self, state):
        """removes a state from the DFA"""
        try:
            self.states.remove(state);
            self.transitionFunction.pop(state);
            print("State " + state + " removed.\n");
        except:
            print("State " + state + " wasn't found.\n");


    def addToAlphabet(self, symbol):
        """Adds a symbol to the alphabet for the DFA"""
        if symbol not in self.alphabet:
            self.alphabet.append(symbol);
            print("Symbol '" + symbol + "' added.");
        else:
            print(symbol + " is already in the alphabet for this DFA.");

        self.printTuple();

    def removeFromAlphabet(self, symbol):
        """removes a symbol from the DFA alphabet"""
        try:
            self.alphabet.remove(symbol);

        except:
            print("Symbol '" + symbol + "' not in alphabet.");


    def addTransition(self, startState, endState, symbol):
        """adds a transition to the DFA's transition function"""
        myTransition = self.transition(endState, symbol);

        if startState not in self.states:
            print("State '" + startState + "' not in DFA.");

        elif endState not in self.states:
            print("State '" + endState + "' not in DFA.");

        elif symbol not in self.alphabet:
            print("Symbol '" + symbol + "' not in alphabet for this DFA.");

        elif self.hasTransition(startState, symbol):
            print("Already a transition from " + startState + " to " + endState + " on " + symbol + ".");

        elif not self.hasTransition(startState, symbol):
            self.transitionFunction[startState].append(myTransition);
            print("Transition from " + startState + " to " + endState + " on " + symbol + " added.");

        


    def hasTransition(self, startState, symbol):
        """see whether the DFA has a transition from the start state on the specified symbol"""
        if startState in self.states:
            for transition in self.transitionFunction[startState]:
                if transition.symbol == symbol:
                    return True;

        return False;

    def getTransition(self, startState, symbol):
        """gets the transition from the specified state on the specified symbol"""
        if startState in self.states:
            for transition in self.transitionFunction[startState]:
                if transition.symbol == symbol:
                    return transition;

        return None

    def removeTransition(self, startState, symbol):
        if startState in self.states:
            for transition in self.transitionFunction[startState]:
                if transition.symbol == symbol:
                    try:
                        transitionFunction[startState].remove(symbol)
                    except:
                        print("Transition from state '" + startState + "' on '" + symbol + "' does not exist!");

    def setStartState(self, newStartState):
        """sets the start state for the DFA"""
        if newStartState in self.states:
            self.startState = newStartState;
            print("Start state is now state '" + newStartState + "'.");

        else:
            print("State " + newStartState + " does not exist in this DFA.");

    
    def addAcceptState(self, newAcceptState):
        """adds a new accept state to the DFA"""
        if newAcceptState not in self.states:
            print("State '" + newAcceptState + "' is not a part of this DFA.");

        else:
            if newAcceptState not in self.acceptStates:
                self.acceptStates.append(newAcceptState);

    
    def removeAcceptState(self, acceptNoMore):
        """removes an accept state from the DFA (state remains a part of the DFA"""
        try:
            self.acceptStates.remove(acceptNoMore);

        except:
            print("State '" + acceptNoMore + "' is not an accept state.");


    def validate(self):
        """Validates that the DFA is in valid form"""
        #make sure each state has a valid symbol
        for state in self.states:
            for symbol in self.alphabet:
                if not self.hasTransition(state, symbol):
                    print("DFA is missing transition from " + state + " on " + symbol + ".");
                    self.printTuple();
                    return False;

        #make sure there is some accept state
        if not self.acceptStates:
            print("DFA needs at least one accept state");
            self.printTuple();
            return False;

        #check valid start state
        if self.startState not in self.States:
            print("DFA has an invalid start state");
            self.printTuple();
            return False;

        #if all these conditions hold, assume the DFA is valid
        print("DFA is valid!");
        return True;




    def convertToRegex(self):
        self.validate();
        #do conversion things

    def getMultipleEdges(self, startState, endState):
        """returns a list containing each symbol for a transition to the specified end state"""
        if (startState not in self.states) or (endState not in self.states):
            print("Start or end state does not exist in DFA. Check your input and try again");
            return;

        #check to see if 
        multipleTransitionList = [];
        for aTransition in self.transitionFunction[startState]:
            if aTransition.endState == endState:
                multipleTransitionList.append(aTransition.symbol);

        return multipleTransitionList;


    def simplifyMultiEdges(self):
        """removes multi-edges from the list of transitions and replaces them with union"""
        for startState in self.states:
            for endState in self.states:

                #union multiple edges
                multiEdges = self.getMultipleEdges(startState, endState);
                unionEdge = "";
                if multiEdges.count() >= 2:
                    unionEdge = " \u222a ".join(multiEdges);

                    #remove edges we've combined into multi edges
                    for edge in multiEdges:
                        self.removeTransition(startState, edge);

                    #add the unioned edge to the transition
                    self.transitionFunction[startState].append(self.transition(endState, unionEdge));

                    
                
                    
    def printTransitions(self):
        """prints the transition table for the DFA"""
        print("\u03B4 = ");
        print("| \t", end = "");
        #print '0th' label row
        for symbol in self.alphabet:
            print(symbol + "\t", end = "");

        print();

        #print each state's transitions
        for rowState in self.states:
            print("|");
            print("| " + rowState + "\t", end = "");
            for symbol in self.alphabet:
                if self.hasTransition(rowState, symbol):
                    print(self.getTransition(rowState, symbol).endState + "\t", end = "");
                else:
                    print("\t", end = "");

            print();


    
        

    def printTuple(self):
        """Prints the formal description for the DFA."""

        print("\nThe current properties of your DFA are...");

        #set of states
        print("         Q = ", end = ""), pprint.pprint(self.states);

        #symbol alphabet
        print("         \u03A3 = ", end = ""), pprint.pprint(self.alphabet);
        
        #transition table
        print("         \u03B4 = (see below)");

        #start state
        print("    Qstart = " + self.startState);

        #accept states
        print("Qaccept(s) = ", end = ""), pprint.pprint(self.acceptStates);

        print();
        self.printTransitions();
        print();