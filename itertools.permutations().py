from itertools import permutations
S,k= input().split()
li=list(permutations(S,int(k)))
for i in sorted(li):
    print("".join(i))
