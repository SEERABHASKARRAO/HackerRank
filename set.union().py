# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=set(map(int,input().split()))
m=int(input())
t=set(map(int,input().split()))
y=l.union(t)
y=list(y)
print(len(y))
