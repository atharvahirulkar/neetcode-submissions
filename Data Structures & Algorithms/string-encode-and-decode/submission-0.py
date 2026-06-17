class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            s_len = len(s)
            encoded_str += str(s_len) + "%" + s

        return encoded_str


    def decode(self, s: str) -> List[str]:
        m=len(s)
        i = 0
        decoded_str = []
        while i < m:
            left = i
            
            while s[i] != "%":
                i+=1
                
            s_len = int(s[left : i])
            start = i + 1
            end = start + s_len
            substr = s[ start:end ]
            decoded_str.append(substr)
            
            i = end

        return decoded_str

