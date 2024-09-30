
#  maximin occurance of 1
l1 = [1,1,0,0,0,1,1,1,1,1,0,0,1,1,1]

count =0
max =0
for i in l1:
    if i ==1:
        count += 1
        if (count >= max):
            max = count

    else :
        # max = count
        count =0

print(max)
                
                
