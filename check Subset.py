# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n=int(input())
    a=set(map(int,input().split()))
    m=int(input())
    b=set(map(int,input().split()))
    if(a.__sub__(b)):
        print("False")
    else:
        print("True")
