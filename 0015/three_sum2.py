class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = - nums[i]
            l = i + 1
            r = n - 1
            checked = set()
            while l < r:
                if nums[l] + nums[r] == target:
                    if nums[l] in checked:
                        l += 1
                    elif nums[r] in checked:
                        r -= 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        checked.add(nums[l])
                        checked.add(nums[r])
                        l += 1
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return triplets
                
print(Solution().threeSum([3,0,-2,-1,1,2]))
# print(Solution().threeSum([-2,0,0,2,2]))