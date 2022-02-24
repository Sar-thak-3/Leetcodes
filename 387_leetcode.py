s = input()
char_count = []
for chr in s[1:len(s)-1]:
    char_count.append([chr,s.count(chr)])
print(char_count)    
for pos,ch in enumerate(char_count):
    if ch[1]==1:
        print(pos)
        break
    elif pos==len(char_count)-1:
        print("-1")
    else:
        continue