# Example file: insertion_sort.py

# Each sorting function should accept a list of integers as the single required
# parameter, as shown below. The input list should be sorted upon completion.
def insertion_sort(nums):
	for i in range(1, len(nums)):
		temp = nums[i]
		j = i
		while j > 0 and nums[j-1] > temp:
			nums[j] = nums [j - 1]
			j -= 1
		nums[j] = temp
