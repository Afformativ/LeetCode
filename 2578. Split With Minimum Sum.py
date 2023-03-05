class Solution:
    def splitNum(self, num: int) -> int:
        digit_counts = Counter(str(num))
        num1 = ""
        num2 = ""
    
        for digit in range(10):

            if str(digit) in digit_counts:
                num1 += str(digit) * (digit_counts[str(digit)] // 2)
                num2 += str(digit) * (digit_counts[str(digit)] // 2)

                if digit_counts[str(digit)] % 2 != 0:
                    if len(num1) < len(num2):
                        num1 += str(digit)
                    else:
                        num2 += str(digit)

        return int(num1) + int(num2)

        
