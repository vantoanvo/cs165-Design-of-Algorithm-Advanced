def merge_sort(nums):
    
    if len(nums) > 1:
        mid = len(nums) // 2
        s1 = nums[:mid]
        s2 = nums[mid:]
        merge_sort(s1)
        merge_sort(s2)
        merge(s1, s2, nums)

def merge(s1, s2, s):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1
    while i < len(s1):
        s[i + j] = s1[i]
        i += 1
    while j < len(s2):
        s[i + j] = s2[j]
        j += 1
