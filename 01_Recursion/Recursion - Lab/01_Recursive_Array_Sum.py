def sum_array(nums, index):
    if index == len(nums) - 1:
        return nums[index]
    return nums[index] + sum_array(nums, index + 1)


nums = [int(x) for x in input().split()]
print(sum_array(nums, 0))
