import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:

            time += 1
            a_time = time + n + 1


            if queue and queue[0][0] == time:
                _, count = queue.popleft()
                heapq.heappush(heap, count)

            if heap:
               count = 1 + heapq.heappop(heap)
               
               if count != 0:
                queue.append((a_time, count))


        return time