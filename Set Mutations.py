# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=set(map(int,input().split()))
for _ in range(int(input())):
    s=input()
    m=set(map(int,input().split()))
    if(s[0]=='i'):
        l.intersection_update(m)
    elif(s[0]=='u'):
        l.update(m)
    elif(s[0]=='s'):
        l.symmetric_difference_update(m)
    else:
        l.difference_update(m)
print(sum(l))
