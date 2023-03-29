# Modulo mqueue
# Disponiliza as operacoes sobre filas de espera

def newq():
    return []
    
def enter(x,f):
    return f+[x]
        
def leave(f):
    if f==newq():
        print("Erro! A fila esta vazia.")
    else:
        return f[1:]
        
def first(f):
    if f==newq():
        print("Erro! A fila está vazia.")
    else:
        return f[0]
        
def empty(f):
    return f==newq()