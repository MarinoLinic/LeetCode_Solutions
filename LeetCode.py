#0. FizzBuzz | Easy | O(1)
for i in range(100):
    out = ""

    if i % 3 == 0:
        out += "Fizz"

    if i % 5 == 0:
        out += "Buzz"

    if i % 7 == 0:
        out += "Bazz"

    # Printing
    if out == "": # JS: console.log(out || i)
        print(i)
    else:
        print(out)


#1. Two Sum | Easy | O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            
            remainder = target - nums[i]
            
            if remainder in hashmap and hashmap[remainder] != i:
                if i < hashmap[remainder]:
                    return [i, hashmap[remainder]]
                else:
                    return [hashmap[remainder], i]
            
            hashmap[nums[i]] = i


#13. Roman to Integer | Easy | O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        n = len(s)
        answer = 0
        
        for i in range(n):
            
            # Avoid index out of range
            if i == n-1:
                answer += roman_numerals[s[i]]
                break
            
            # Check if the character at right of current character is bigger or smaller
            if roman_numerals[s[i]] >= roman_numerals[s[i+1]]:
                answer += roman_numerals[s[i]]
            else:
                answer -= roman_numerals[s[i]]
                
        return answer
        