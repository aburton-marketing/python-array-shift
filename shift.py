nums = [0,1,2,10,0,0]
insert = 20
pos = 0
def shift(nums, pos, insert):
  i = len(nums) / 2
  while True:
    if i == 0:
      break
    else:
      nums[i + 1], nums[i] = nums[i], nums[i + 1]
    i -= 1
  nums[pos] = insert
  return nums
