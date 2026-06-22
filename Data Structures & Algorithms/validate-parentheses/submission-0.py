class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        check = { ")":"(" , "}":"{" , "]":"[" }

        for b in s:

            if b == "(" or b == "{" or b == "[" :
                stack.append(b)

            else:
                if not stack:
                    return False
                
                
                to_check = stack[-1]

                if check[b] != to_check:
                    return False

                stack.pop()


        if not stack:
            return True

        else:
            return False

                

                