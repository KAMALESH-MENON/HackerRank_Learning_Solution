if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        stmt= list(input().split())
        if stmt[0]=="insert":
            l.insert(int(stmt[1]),int(stmt[2]))
        elif stmt[0]=="remove":
            l.remove(int(stmt[1]))
        elif stmt[0]=="sort":
            l.sort()
        elif stmt[0]=="print":
            print(l)
        elif stmt[0]=="append":
            l.append(int(stmt[1]))
        elif stmt[0]=="reverse":
            l.reverse()
        elif stmt[0]=="pop":
            l.pop(len(l)-1)
