# статическая типизация
from typing import List, Dict, Tuple

s: str   # это подсказка, какой тип будет использоваться
n: int = 1 #

def is_equal(n1: int,n2: int)->bool:
    return n1 == n2

print(is_equal('2',3))


lst: List[int]
lst = [2,3,4]
d: Dict[str,int]
t: List[Tuple[int, int]]
