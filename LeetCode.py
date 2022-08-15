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