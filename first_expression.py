from automata.fa.dfa import DFA

dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'qe'},
    input_symbols={'b', 'a', 'a', 'c', 'B', 'A', 'A', 'C'},
    transitions={
        'q0': {'b': 'q1', 'B': 'q1', 'a': 'qe', 'a': 'qe', 'c': 'qe', 'A': 'qe', 'A': 'qe', 'C': 'qe'},
        'q1': {'a': 'q2', 'A': 'q2', 'b': 'qe', 'B': 'qe', 'a': 'qe', 'b': 'qe', 'A': 'qe', 'C': 'qe'},
        'q2': {'a': 'q3', 'A': 'q3', 'a': 'qe', 'A': 'qe', 'b': 'qe', 'b': 'qe', 'B': 'qe', 'C': 'qe'},
        'q3': {'c': 'q4', 'C': 'q4', 'a': 'qe', 'A': 'qe', 'b': 'qe', 'a': 'qe', 'B': 'qe', 'A': 'qe'},
        'q4': {'b': 'qe', 'a': 'qe', 'a': 'qe', 'c': 'qe', 'B': 'qe', 'A': 'qe', 'A': 'qe', 'C': 'qe'},
        'qe': {'b': 'qe', 'a': 'qe', 'a': 'qe', 'c': 'qe', 'B': 'qe', 'A': 'qe', 'A': 'qe', 'C': 'qe'}
    },
    initial_state='q0',
    final_states={'q1', 'q2', 'q3', 'q4'}
)

def es_valida(cadena):
    try:
        dfa.read_input(cadena)
        return True
    except:
        return False
    
print(es_valida("baaC"))