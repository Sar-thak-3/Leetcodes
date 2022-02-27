tar = input()
tar = tar[1:len(tar)-1]
tar = tar.split(",")
target = list(map(lambda x:int(x),tar))
ar = input()
ar = ar[1:len(ar)-1]
ar = ar.split(",")
arr = list(map(lambda x:int(x),ar))

def canMadeEqual(arr,tar,n):
    arr.sort()
    target.sort()
    for i in range(n):
        if (arr[i] != target[i]):
            return False
    return True

if (canMadeEqual(arr,target,len(target))):
    print( "Yes")
else:
    print("No")