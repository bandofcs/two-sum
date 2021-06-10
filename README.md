### Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

**Example 1:**
```py
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```py
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```py
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

* ```py2 <= nums.length <= 104```
* ```py-109 <= nums[i] <= 109```
* ```py-109 <= target <= 109```
* **Only one valid answer exists.**
 

**Follow-up:** Can you come up with an algorithm that is less than O(n<sup>2</sup>) time complexity?
