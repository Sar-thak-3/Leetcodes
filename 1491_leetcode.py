salary = input()
salary = salary[1:len(salary)-1]
salary = salary.split(",")
sal = list(map(lambda x: int(x),salary)) 
print(sal)
sal.remove(min(sal))
sal.remove(max(sal))
avg = f"{sum(sal)/len(sal):.5f}"
print(avg)