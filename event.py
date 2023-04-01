# Modulo event
# Disponibiliza as operacoes necessarias para a criacao e
# manipulacao de eventos

def evt(t, k, counts):
    return [t, k, counts]

def time(e):
    return e[0]

def kind(e):
    return e[1]

def counts(e):
    return e[2]
