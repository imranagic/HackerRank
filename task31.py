from itertools import combinations_with_replacement

s,k = input().split()

l = sorted([sorted(t) for t in list(combinations_with_replacement(s,int(k)))])

for t in l:
    print(''.join(t))
     