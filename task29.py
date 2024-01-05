n,m = [int (x) for x in input().split()]

l = list(map(int, input().split()))

a = set(map(int, input().split()))

b = set(map(int, input().split()))

hap = 0

for i in l:
    if i in a:
        hap += 1
    elif i in b:
        hap -= 1
print(hap)


