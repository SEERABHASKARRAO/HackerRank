# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
l=list(map(int,input().split()))
n=int(input())
sum1=0
for i in range(n):
    a,b=map(int,input().split())
    if(a in l):
        sum1+=b 
        l.remove(a)
print(sum1)
