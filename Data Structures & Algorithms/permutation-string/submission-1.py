from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:n1])

        if c2 == c1 :
            return True


        left = 0
        for right in range(n1, n2):
            c2[s2[right]] += 1

            c2[s2[left]] -= 1
            if c2[s2[left]] == 0:
                del c2[s2[left]]

            left += 1
            
            if c2 == c1:
                return True


        return False

