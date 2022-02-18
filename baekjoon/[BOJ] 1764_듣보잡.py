import sys

input = sys.stdin.readline
N, M = map(int, input().split())
no_hear = [input().strip() for _ in range(N)]
no_see = [input().strip() for _ in range(M)]

no_hear_no_see = sorted(list(set(no_hear) & set(no_see)))

print(len(no_hear_no_see))
for name in no_hear_no_see:
    print(name)
