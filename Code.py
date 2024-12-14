'''
Author: Alexandra Stratton, Riley Sirimongkhon-Dyck, Sophia Medallada
Date: 12/13/2024
Assignment: 510 Final Project
Last modified: 12/13/2024
Purpose: Part 4
'''
def accept(s):
    transitions = {('J', ''): ['H','A'],
                   ('H', 'h'): ['PH'],
                   ('A', 'a'): ['PA'],
                   ('PH', 't'): ['RH'],
                   ('PH', 's'): ['BH'],
                   ('PH', 'y'): ['A'],
                   ('PH', 'x'): ['H'],
                   ('PH', 'f'): ['FA'],
                   ('PH', 'o'): ['IA'],
                   ('PA', 't'): ['RA'],
                   ('PA', 's'): ['BA'],
                   ('PA', 'y'): ['H'],
                   ('PA', 'x'): ['A'],
                   ('PA', 'f'): ['FH'],
                   ('PA', 'o'): ['IH'],
                   ('BH','m'): ['MH'],
                   ('BH','n'): ['NH'],
                   ('BA','m'): ['MA'],
                   ('BA','n'): ['NA'],
                   ('NH','r'): ['H','A'],
                   ('NH','o'): ['IA'],
                   ('NH',''): ['FH'],
                   ('MH', ''): ['FH','IA'],
                   ('NA','r'): ['H','A'],
                   ('NA','o'): ['IH'],
                   ('NA',''): ['FA'],
                   ('MA',''): ['FA','IH'],
                   ('FH',''): ['IH'],
                   ('FH','s'): ['BH'],
                   ('FA',''): ['IA'],
                   ('FA','s'): ['BA'],
                   ('RH','g'): ['IH'],
                   ('RH','d'): ['H'],
                   ('RA','g'): ['IA'],
                   ('RA','d'): ['A'],
                   ('IH','i'): ['H','A'],
                   ('IA','i'): ['H','A'],}

    state = 'J'
    accepting_states = ['MH', 'NH', 'MA', 'NA']  
    possible_states = [state]
    char_list = list(s)
    terminals = ['h','a','s','x','y','m','n','r','o','t','g','d','d','i']
    count = 0
    while char_list:
        c = char_list[0] 
        next_possible_states = []
        next_states = []
        remove = False
        for i in range(len(possible_states)):
            if (possible_states[i], c) in transitions:
                next_states = transitions[possible_states[i], c]
                for j in range(len(next_states)):
                    next_possible_states.append(next_states[j])
                remove = True
            elif (possible_states[i], '') in transitions:
                next_states = transitions[possible_states[i], '']
                for j in range(len(next_states)):
                    next_possible_states.append(next_states[j])
        if c not in terminals:
            'rejected'
        if next_possible_states == []:
            return 'rejected'
        if remove:
            c = char_list.pop(0)
        possible_states = next_possible_states
    for state in possible_states:
        if state in accepting_states:
            return 'accepted'
    return 'rejected'

def main():
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input == 'q':
            break
        result = accept(user_input)
        print(f"Result: {result}")
main()
