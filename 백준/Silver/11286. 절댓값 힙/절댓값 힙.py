import sys
import heapq

N = int(sys.stdin.readline())

min_heap = []
max_heap = []

for i in range(N):
	a = int(sys.stdin.readline())
	if a > 0:
		heapq.heappush(min_heap, a) 
	elif a < 0:
		heapq.heappush(max_heap, -a) 
	else:
		if min_heap: 
			if max_heap: #exist both min & max heap
				if min_heap[0] < max_heap[0]:
					print(heapq.heappop(min_heap))
				else:
					print(-1 * heapq.heappop(max_heap))
			else:
				print(heapq.heappop(min_heap))
		elif max_heap: # only exist max heap
			print(-1 * heapq.heappop(max_heap))
		else: # not exist both min & max heap
			print(0)