# SKIL6 - Lárus og Jónas

# 1. Heildi og flatarmál

import math

class Stak:
    def __init__(self):
        self.formerki = "+"
        self.value = 1
        self.x = False
        self.veldi = 1

        self.heildad = False

    def print(self):
        print(self.formerki, self.value, self.x, self.veldi)

    def heilda(self):
        if self.heildad:
            return 0

        self.heildad = True
        if self.x is False:
            self.x = True

        elif self.x:
            self.veldi += 1
            self.value = self.value / self.veldi

    def reikna(self, x):
        v = float(self.formerki + str(self.value))

        if self.x:
            x = math.pow(x, self.veldi)

            return v * x

        else:
            return v

    def get_stak(self):
        s = self.formerki
        if self.x:
            if self.value == 1:
                s += "x"

            else:
                s += str(self.value) + "x"

        else:
            s += str(self.value)

        if self.veldi > 1 or self.veldi < 0:
            s += str(self.veldi)

        if self.veldi == 0:
            s = 0

        return s

class Fall:
    def __init__(self, f):
        self.fall = []

        self.make(f)

    def flatarmal_milli_two(self, other, x, x2):
        return self.flatarmal(x, x2) - other.flatarmal(x, x2)

    def reikna(self, x):
        s = 0
        for a in self.fall:
            s += a.reikna(x)

        return s

    def flatarmal(self, x, x2):
        self.heilda()

        return self.reikna(x) - self.reikna(x2)

    def heilda(self):
        for a in self.fall:
            a.heilda()

        return self.get_fall()

    def make(self, f):
        s = ""
        fall = []
        for a in f:
            if a in ["+", "-"]:
                fall.append(s)
                s = ""
            s += a

        fall.append(s)
        try:
            fall.remove("")
        except:
            pass

        for a in fall:
            s = Stak()
            x_found = False
            x = False
            if "x" in a:
                x = True
                s.x = True
            for b in a:
                if b == "x":
                    x_found = True

                if b in ["-", "+"]:
                    s.formerki = b

                elif b.isdigit() and (x is False or x_found is False):
                    s.value = int(b)

                elif b.isdigit() and (x_found is True):
                    s.veldi = int(b)

            self.fall.append(s)

    def print(self):
        for a in self.fall:
            a.print()

    def get_fall(self):
        s = ""
        for a in self.fall:
            s += a.get_stak()

        return s


fallF = input("Sláðu inn fall f(x) = ")
fallG = input("Sláðu inn fall g(x) = ")

f = Fall(fallF)
g = Fall(fallG)

efrimork = int(input("Sláðu inn x fyrir efri mörk svæðis: "))
nedrimork = int(input("Sláðu inn x fyrir neðri mörk svæðis: "))

utkoma = f.flatarmal_milli_two(g, efrimork, nedrimork)

print("Flatarmálið milli f(x) og g(x) er: ", utkoma)


# 2. Memoization
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


print("Stærsta summa þríhyrningsins er",triangle(lines))
