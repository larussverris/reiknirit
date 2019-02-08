from itertools import *

staf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def strengur(n):
    listi = []
    l = list(combinations(staf, n))
    for a in l:
        s = ""
        for x in a:
            s += x
        listi.append(s)

    return listi

def bubble(items):

    while True:
        c = 0
        p = 1
        swap = False
        for a in range(len(items)-1):
            if items[c] > items[p]:
                swap = True
                items[c], items[p] = items[p], items[c]


            c += 1
            p += 1

        if swap is False:
            break


    return items

p = strengur(3)
for a in p:
    print(a)
input("Enter to continue")
print("----------------------------")
p.reverse()
print(p)
input("Enter to continue")
print("----------------------------")
p = bubble(p)
print(p)
input("Enter to continue")



