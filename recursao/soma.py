
def somar(nums: list):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + somar(nums[1:])


print(somar([1, 2, 3]))
