lines, num, nums = open('input.txt', 'r').readlines(), 0, []
for s in lines :
    nums.append(num if s == "\n" else 0)
    num += -num if s == "\n" else int(s)    
nums.sort(reverse=True)
print(nums[0], nums[0]+nums[1]+nums[2])