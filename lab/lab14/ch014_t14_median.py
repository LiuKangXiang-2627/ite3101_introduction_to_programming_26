from typing import List

def median(lst):
    sorted_lst=sorted(lst)    
    if len(sorted_lst) % 2 ==0:
        index_1 = 