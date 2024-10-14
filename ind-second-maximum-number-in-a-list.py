if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    [res.append(x) for x in arr if x not in res]
    res.sort()
    print(res[len(res)-2])
