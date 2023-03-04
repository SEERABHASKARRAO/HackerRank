
n=int(input())
l=set(map(int,input().split()))
m=int(input())
t=set(map(int,input().split()))
y=l.symmetric_difference(t)
y=list(y)
print(len(y))
