# array right shift that maintains order
# copyright 2020 aaron burton


nums = [20,0,1,2,10,0]
insert = 30
pos = 0

def aShift(nums, pos, insert):
	i = len(nums) - 2
	while i >= pos:
		print(pos, i, nums)
		nums[i + 1], nums[i] = nums[i], nums[i + 1]
		i -= 1
	nums[pos] = insert
	return nums

z = 0
while True:
	if nums[z] == 0:
		pos = z + 1
		aShift(nums, pos, 0)
		z += 1
	z += 1
	if z >= len(nums)-1:
		break
