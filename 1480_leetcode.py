nums = input()
nums = nums[1:len(nums)-1]
nums = nums.split(",")
sum = 0
new_list = []
for n in nums:
    sum = sum+int(n)
    new_list.append(sum)
print("[",end='')
for n in new_list:
    if n == new_list[len(new_list)-1]:
        print(n,end="")
    else:
        print(n,end=',')    
print("]")    