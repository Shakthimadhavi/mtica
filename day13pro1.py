##n=input()
##temp=n.split()
##ans=[len(i) for i in temp]
##print(*ans)


def solveProblem(s):
    lst=s.split()
    return[len(i) for i in lst]
inp=input()
print(*solveProblem(inp))
