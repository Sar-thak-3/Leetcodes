candies = input("Enter candies each child have: ")
candies = candies[1:len(candies)-1]
candies = candies.split(",")
candy = list(map(lambda x:int(x),candies))
extra_candies = int(input("Enter extra candies: "))
lst = []
for n in candy:
    if n+extra_candies >= max(candy):
        lst.append(True)
    else:
        lst.append(False)    
print(lst)        