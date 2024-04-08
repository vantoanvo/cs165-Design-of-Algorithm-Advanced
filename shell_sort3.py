import math
def shell_sort3(nums):
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
    for i in nums:
        print(i)

def generate_sequence(nums):
    seq = [1]
    index_of_last = 0
    last_exp_3 = 1
    n = len(nums)
    while seq[-1] < n:
        if seq[index_of_last]*2 <last_exp_3*3:
            seq.append(seq[index_of_last]*2)
            index_of_last += 1
        else:
            seq.append(last_exp_3*3)
            last_exp_3 *= 3
    seq.pop()
    return seq