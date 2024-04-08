
def hybrid_sort2(nums):
    h = len(nums)**0.4
    if len(nums) > h:
        mid = len(nums) // 2
        s1 = nums[:mid]
        s2 = nums[mid:]
        hybrid_sort2(s1)
        hybrid_sort2(s2)
        merge(s1, s2, nums)
    else:
        insertion_sort(nums)

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

def insertion_sort(nums):
	for i in range(1, len(nums)):
		temp = nums[i]
		j = i
		while j > 0 and nums[j-1] > temp:
			nums[j] = nums [j - 1]
			j -= 1
		nums[j] = temp
