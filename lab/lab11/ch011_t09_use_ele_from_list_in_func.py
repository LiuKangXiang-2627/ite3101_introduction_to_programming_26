from typing import List


def list_function(y: List[int]) -> List[int]:
    print(y[0])
    return y[1]
n = [3,5,7]
print(list_function(n))
