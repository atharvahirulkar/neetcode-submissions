from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = Counter()

        required = len(need)
        formed = 0
        
        left = 0
        min_len = float("inf")
        ans = ""    


        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1


            while formed == required :
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left : right +1]


                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return ans


        