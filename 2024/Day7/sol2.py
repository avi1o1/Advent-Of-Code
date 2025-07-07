def checkValid(val, nums, curr):
    if len(nums) == 0:
        return val == curr

    return checkValid(val, nums[1:], curr+nums[0]) or checkValid(val, nums[1:], curr*nums[0]) or checkValid(val, nums[1:], int(str(curr)+str(nums[0])))

ans = 0
with open("Day7/input2.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        val, tmp = line.split(': ')
        nums = tmp.split()
        nums = [int(num) for num in nums]

        if checkValid(int(val), nums[1:], nums[0]):
            # print(int(val))
            ans += int(val)
print(ans)