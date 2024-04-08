import math
def shell_sort4(nums):
    #calculate gap 
    s = generate_sequence(nums)
    for gap in s:
        while gap > 0:
            for i in range(gap, len(nums)): 
                temp = nums[i]
                j = i
                while j >= gap and temp < nums[j - gap]:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = 0

def generate_sequence(nums):
    s = []
    n = 0
    result = 1
    while result < len(nums):
        s.insert(0, result)
        result = 4**(n+1) + 3*2**n + 1
        n += 1
    return s
        