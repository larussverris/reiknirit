import itertools

#allar mögulegir strengir af lengd n úr enska stafrófinu

def stafrof(lengd):
    stafir = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    listi = list(itertools.combinations(stafir, 3))
    for x in listi:
        print(*x)
        
        
#stafrof(3)
