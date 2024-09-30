'''An anagram is a word or phrase formed by rearranging the letters of another'''

a ="Silent"
a = a.lower()
b  = "Listen"
b = b.lower()

print(len(a)==len(b))
print(sorted(a)==sorted(b))

is_anagaram = True
for i in a:
    if i not in b:
        print("fasle ")
        is_anagaram = False
        break
    
if(is_anagaram):
    print("true")


