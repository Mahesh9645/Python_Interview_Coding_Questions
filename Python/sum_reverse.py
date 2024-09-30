#ivenn list is to reverse and print even position digits

a =[10,20,30,40,50,60]
b = []

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print(f"reverse array,{b}")

for i in range(len(b)-1):
    if i% 2 ==0:
        print(b[i])