n = int(input())
for i in range(n):
    a, b = map(str, input().split())

    try:
        print (int(a)//int(b))
    except ZeroDivisionError as e:
        print( "Error Code:",e)
    except ValueError as v:
        print( "Error Code:",v)
    
    