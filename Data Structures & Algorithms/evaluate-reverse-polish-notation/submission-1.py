class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operate = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operate:
                numbers.append(int(i))
            
            else:
                num2 = numbers.pop()
                num1 = numbers.pop()

                if i == "+":
                    numbers.append( num1 + num2 )
                
                elif i == "-":
                    numbers.append( num1 - num2)

                elif i == "*":
                    numbers.append( num1 * num2 )
                
                else:
                    numbers.append( int(num1 / num2) )


            
        return numbers[-1]

