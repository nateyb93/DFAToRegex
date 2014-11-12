"""defines the main line for the program"""
import dfa
import state
import sys
import transition

myDFA = dfa.dfa();

"Begin functions"
def main():
    """Defines the main execution line for the program"""
    print("Welcome to the DFA->RegEx converter program");
    
    print("A default DFA has been created for you: ");
    myDFA.prettyPrint();

    option = 0;

    while(option != 'x'):
        option = input("What would you like to do?\n"
                     + "Press 1 to add/remove a state\n"
                     + "Press 2 to add/remove a symbol to/from the alphabet\n"
                     + "Press 3 to add/remove a transition to a state\n"
                     + "Press 4 to set the start state for the DFA\n"
                     + "Press 5 to add/remove accept states to/from the DFA\n"
                     + "Press 0 to convert to Regex\n"
                     + "Press x to exit\n");
        handle_input(option);


def handle_input(option):
    """handles user input"""
    if(option == '1'):
        option = input("Press 0 to remove a state or 1 to add a state:\n");
        changeStates(option);

    elif(option == '2'):
        option = input("Press 0 to remove a symbol from the alphabet or 1 to add a symbol:\n");
        changeAlphabet(option);

    elif(option == '3'):
        option = input("Press 0 to remove a transition from the DFA or 1 to add a transition:\n");
        changeTransitions(option);

    elif(option == '4'):
        option = input("Type in the name of the state you wish to set as the start state:\n");
        changeStartState(option);

    elif(option == '5'):
        option = input("Press 0 to remove an accept state or 1 to add an accept state:\n");
        changeAcceptStates(option);

    elif(option == '0'):
        DFAToRegex();

    elif(option == 'x'):
        sys.exit(0);

    else:
        print("I'm sorry, I didn't get that.");


def changeStates(option):
    """updates the states for the DFA object"""
    if option == '0':
        stateName = input("Type the name of the state you wish to delete:\n");
        myDFA.removeState(stateName);

    elif option == '1':
        stateName = input("Type the name of the state you wish to add:\n");
        myDFA.addState(stateName);

    return;


def changeAlphabet(option):
    """updates the alphabet for the dfa object"""
    if option == '0':
        symbol = input("Type the symbol you wish to remove from your alphabet:\n");
        myDFA.removeFromAlphabet(symbol);
    elif option == '1':
        symbol = input("Type the symbol you wish to add to your alphabet:\n");
        myDFA.addToAlphabet(symbol);
    return;


def changeTransitions(option):
    """updates the transitions for the dfa object"""
    if option == '0':
        stateName = input("Type the name of the state you wish to remove a transition from:\n");
        startState = myDFA.getState(stateName);
        symbolToRemove = input("Type the symbol of the transition to remove:\n");
        startState.removeTransition(symbolToRemove);
        
    elif option == '1':
        stateName = input("Type the name of the state you wish to add a transition to:\n");
        startState = myDFA.getState(stateName);
        symbolToAdd = input("Type the symbol of the tranition to add:\n");
        endState = input("Type the name of the state for the transition to end at:\n");
        startState.addTransition(endState, symbolToAdd);

    myDFA.prettyPrint();
    return;


def changeStartState(option):
    """updates the start state for the dfa object"""
    return;


def changeAcceptStates(option):
    """updates the accept states for the dfa object"""
    return;


def DFAToRegex():
    """converts the dfa object into a regex string/"""
    return;	
"end functions"

main();