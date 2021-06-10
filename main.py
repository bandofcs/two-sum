class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict={}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                return [new_dict[nums[i]],i]
            else:
                newkey=target-nums[i]
                new_dict[newkey]=i  
