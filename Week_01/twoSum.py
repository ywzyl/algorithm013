class Solution:
    def twoSum(self, nums, target):
        # 思路：嵌套遍历，内层遍历只遍历外层index之后的列表，排除重复，时间复杂度为O(n*2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]  + nums[j] == target:
                    return [i, j]
        return []

    def twoSumT(self, nums, target):
        # 思路：先排序，接着用双指针从列表两边往中间遍历
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(temp) - 1

        while i<j:
            if (temp[i] + temp[j]) > target:
                j = j - 1
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            else:
                break
        
        p = nums.index(temp[i])
        nums.pop(p) # 此处弹出是防止temp[i]和temp[j]是相同的值，比如7+7=14
        k = nums.index(temp[j])
        if k >= p:
            k = k+1
        return [p, k]
