# Modulo m_events - versao revista
# Disponibiliza as operacoes necessarias para a criacao e
# manipulacao de eventos

def evt(t,k,c):
    return [t,k,c]
    
def time(e):
    return e[0]
    
def kind(e):
    return e[1]
    
def car(e):
    return e[2]