from fractions import gcd, Fraction as f
from functools import reduce
import re
from sys import argv
from sympy import Matrix

def dictjoin(c, b):
    '''joins two dictionaries, adding values of duplicate entries'''
    a = c.copy()
    for i in b:
        if i in a:
            a[i] += b[i]
        else:
            a[i] = b[i]
    return a
def elements(compound):
    '''converts a compound into a dictionary'''
    d = {}
    ion = {}
    c = compound[:]
    if '(' in compound:
        pattern = r"(?P<rest1>.*)\((?P<ion>.*)\)(?P<n>\d+)(?P<rest2>.*)"
        m = re.match(pattern, compound)
        if m.group('rest1'): c = m.group('rest1')
        else: c = m.group('rest2')
        n = int(m.group('n'))
        ion = elements(m.group('ion'))
        for i in ion:
            ion[i] *= n
    c = re.findall(r"[A-Z][a-z]*[0-9]*", c)
    for i in c:
        a = re.match(r'([A-Za-z]+)([0-9]*)', i).groups()
        if a[1] == "":
            d[a[0]] = 1
        else:
            d[a[0]] = int(a[1])
    d = dictjoin(d, ion)
    return d



def splitter(string):
    left, right = [[elements(compound.strip()) for compound in side.strip().split("+")] for side in string.split("->")]
    return (left, right)

def parse(string):
    left, right = splitter(string)
    if reduce(dictjoin, left).keys() != reduce(dictjoin, right).keys():
        raise Exception("There are elements that don't appear on both sides of the equation!")
    eq = []
    for e in reduce(dictjoin, left).keys():
        line = []
        for compound in left:
            if e in compound:
                line.append(compound[e])
            else:
                line.append(0)
        for compound in right:
            if e in compound:
                line.append(-compound[e])
            else:
                line.append(0)
        eq.append(line)
    return(Matrix(eq).nullspace())

def solve(eq):
    ans = parse(eq)
    if len(ans) == 1:
        ans = ans[0].T
        for i in range(len(ans)):
            ans *= ans[i].q
        ans = [i.p for i in ans]
    else:
        ans = [i.T for i in ans]
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i] *= ans[i][j].q
        ans = [Matrix([j.p for j in i]) for i in ans]
        ans2 = reduce(lambda a, b: a + b, ans)
        if all(i > 0 for i in ans2): ans = [i for i in ans2]
        else:
            print("no mas")
            ans = [list(i) for i in ans]
    return ans

if len(argv) == 1:
    a = input("Enter a formula\n")
    while ('->' in a):
        print(solve(a))
        a = input("Enter a formula\n")
else:
    print (solve(argv[1]))

#output(gauss(a))
