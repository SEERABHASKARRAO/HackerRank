# Enter your code here. Read input from STDIN. Print output to STDOUT\
n,x=map(int,input().split())
a=[]
for i in range(x):
    a.append(list(map(float,input().split())))
t=zip(*a)
for i in t:
    print(sum(i)/len(i))
