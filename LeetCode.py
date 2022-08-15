#1. Two Sum
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


# Roman to Integer
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
        