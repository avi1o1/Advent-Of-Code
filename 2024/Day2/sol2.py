ans = 0

def checkMonotonous(nums):
    N = len(nums)

    if nums[0] > nums[1]:
        for i in range(N-1):
            if nums[i] < nums[i+1]:
                return 0
    
    elif nums[0] < nums[1]:
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                return 0
    
    else:
        return 0
    
    return 1

def checkClose(nums):
    N = len(nums)

    for i in range(N-1):
        if nums[i] - nums[i+1] > 3 or nums[i] - nums[i+1] < -3 or nums[i] - nums[i+1] == 0:
            return 0

    return 1

with open('Day2/input1.txt') as f:
    lines = f.readlines()

    for line in lines:
        nums = line.split()
        nums = [int(x) for x in nums]

        if checkMonotonous(nums) and checkClose(nums):
            ans += 1
            continue

        for i in range(len(nums)):
            x = nums.pop(i)

            val = checkMonotonous(nums) and checkClose(nums)
            if val == 1:
                ans += 1
                break

            nums.insert(i, x)

print(ans)