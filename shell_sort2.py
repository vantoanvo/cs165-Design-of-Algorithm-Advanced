import math
def shell_sort2(nums):
    #calculate gap 
    k = math.ceil(math.log(len(nums), 2))
    for m in range(k, -1, -1):
        gap = (2**m) + 1
        if m == 0:
            gap = 1
        while gap > 0:
            for i in range(gap, len(nums)): 
                temp = nums[i]
                j = i
                while j >= gap and temp < nums[j - gap]:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = 0
