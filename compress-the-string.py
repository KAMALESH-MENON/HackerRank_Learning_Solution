from itertools import groupby
string = input()
res = []
for key, group in groupby(string):
    count = len(list(group))
    res.append(f"({count}, {key})")
print(" ".join(res))