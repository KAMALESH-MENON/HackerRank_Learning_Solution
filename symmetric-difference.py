m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

print(*sorted(a ^ b), sep="\n")
