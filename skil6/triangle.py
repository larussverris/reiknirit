
#triangle euler 67 - Lárus Arnar


with open('triangle.txt', 'r') as f:   #opna textaskjal (þarf að breyta nafninu á skjalinu hér!!!)
    lines = [list(map(int, line.split())) for line in f] # býr til lista af listum


def triangle(listi):
    if len(listi) == 1:
        return int(listi[0][0]) # skilar fyrsta item í fyrsta listanum
    else:
        memo = [] # memo listi fyrir memoization
        for x in range(0,len(listi[-1])-1): # loopar í gegn um listann öfugt með range lykkju
            memo.append(max(listi[-1][x],listi[-1][x+1])) # tekur 2 tölur í einu og bætir stærri tölunni í memo listann
        listi[-2] = [x+y for x, y in zip(memo, listi[-2])] # tekur listann á undan(næst seinasta línan í skjalinu) og memo listann og summar þá saman
        memo.clear() # hreinsar memo listann
        del(listi[-1]) # eyðir seinustu línunni
        return triangle(listi) # endurkvæmni


print(triangle(lines))
