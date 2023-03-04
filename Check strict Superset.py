# Enter your code here. Read input from STDIN. Print output to STDO
a=set(map(int,input().split()))
m=int(input())
flag=1
for i in range(m):
    b=set(map(int,input().split()))
    if(a.issuperset(b)):
        flag=0
    else:
        print("False")
        flag=1
        break
if(flag==0):
    print("True")
    
