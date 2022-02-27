n = input()
n = n.split(" ")
nums = list(map(lambda x:int(x),n))   
xor_sum = 0
for itm in nums:
    xor_sum += itm

import itertools
xoor = 0
for i in range(2,len(nums)+1):
    list2 = list(itertools.combinations(nums,i))
    print(list2)
    for itm in list2:
        xoor = 0
        for sub in itm:
            xoor = xoor^sub    
        xor_sum += xoor    
print(xor_sum)