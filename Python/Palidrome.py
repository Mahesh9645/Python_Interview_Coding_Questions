# String 

s = "madam"
s1 = s[::-1]
print(s == s1)

# mryhod 2

s = "mom"
s1 =""
for i in range(len(s)-1,-1,-1):
    s1 +=s[i]
print(s1 == s)

# with list

a =121
n=a
rev =0
while a > 0:
    rev  = rev * 10
    rev =rev + a %10
    a =a//10
print(rev)
if (rev == a):
    print("yes")
else:
    print("no")