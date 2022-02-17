def spy_game(nums):
    for x in range(0, len(nums)):
        if nums[x] == 0:
            if nums[x+1] == 0 and x+1 < len(nums):
                if nums[x+2] == 7 and x+2 < len(nums):
                    return True
    return False
li = [int(x) for x in input().split()]
print(spy_game(li))