str=input("enter the string:")
count=0
for i in str:
    if i in 'aeiouAEIOU':
        count+=1
        print("the number of vowels in",str,"is",count)


