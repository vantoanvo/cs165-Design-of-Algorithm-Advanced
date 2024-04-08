import math
def shell_sort1(nums):
    #calculate gap 
    k = math.ceil(math.log(len(nums), 2))
    for m in range(1, k):
        gap = len(nums)//(2**m)
        while gap > 0:
            for i in range(gap, len(nums)): 
                temp = nums[i]
                j = i
                while j >= gap and temp < nums[j - gap]:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = 0