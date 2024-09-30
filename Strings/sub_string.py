s = "aaabbbbbcccaabbccdddaaccbb"
sub_string = "c"

flag = False
pos =-1

n =len(s)

while True:
    pos = s.find(sub_string,pos+1,n)
    if pos ==-1:
        break
    print(pos)
    flag =True

if flag ==False:
    print("not found")