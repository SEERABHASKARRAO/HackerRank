def merge_the_tools(string, k):
  
    for i in range(0,len(string),k):
        a=''
        b=string[i:i+k]
        for j in b:
            if j not in a:
                a+=j
        print(a)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
