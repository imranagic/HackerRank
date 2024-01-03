n = int(input())

le = set(map(int, input().split()))

b = int(input())

lf = set(map(int, input().split()))

print(len(le.union(lf)))