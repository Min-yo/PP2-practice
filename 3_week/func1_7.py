def has_33(nums):
    for x in range(0, len(nums)):
        if nums[x] == 3:
            if nums[x+1] == 3:
                return True
    return False
li = [int(x) for x in input().split()]
print(has_33(li))