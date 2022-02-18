import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
dq = deque([n for n in range(1,N+1)])
num_list = list(map(int,sys.stdin.readline().split()))

def choose(deque):
    deque.popleft()
def move_left(deque):
    deque.append(deque.popleft())
def move_right(deque):
    deque.appendleft(deque.pop())

cnt = 0
for num in num_list:
    while True:
        if num == dq[0]:
            choose(dq)
            break
        elif (dq.index(num) < len(dq)/2):  # num의 index가 dq 중간보다 앞에 있는 경우
            while num != dq[0]:
                move_left(dq)
                cnt += 1
        else:
            while num != dq[0]:
                move_right(dq)
                cnt += 1
print(cnt)