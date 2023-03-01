# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
l=set(map(int,input().split()))
n=int(input())
l1=set(map(int,input().split()))
p=l.difference(l1)
q=l1.difference(l)
q=list(q)
p=list(p)
p.extend(q)
p.sort()
for i in p:
    print(i)
