from typing import Tuple, TypeVar
T1 = TypeVar('T1')
T2 = TypeVar('T2')

def inverter_tupla(t: Tuple[T1,T2]) -> Tuple[T2,T1]:
    '''Inverte a posição dos elementos de uma tupla'''
    return (t[1],t[0])

print(inverter_tupla(("ola", "mundo")))
print(inverter_tupla((1, "joão")))
print(inverter_tupla(("mendes", 2)))