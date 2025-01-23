import sys
import heapq
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    min_heap = []
    max_heap = []
    nums = dict()

    for j in range(N):
	    oper, num_ = input().split()
        num = int(num_)
        
	    if oper == "I":
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
		        heapq.heappush(min_heap, num) 
		        heapq.heappush(max_heap, -num)
                
	    elif oper == "D":
		    if num == 1: 
