print("Enter the values of list one by one \t")
n=(int(input("Enter the size of the list \t")))
# initalizing a blank list
mylist = []

for i in range(n):
    mylist.append(int(input("Enter the number \t")))

print(f"List is {mylist} \n")

# to creat a copy of list we need to add colon inside the bracket, otherwise
# when i reverse my reverselist, mylist also get reversed
reverselist1=mylist[:]
reverselist1.reverse()
print(f"The reversed list  of {mylist} \t is {reverselist1} \n")
reverselist2=mylist[::-1]
print(f"Reverse of list using slicing will be {reverselist2} \n")

reverselist3=mylist
for i in range(len(reverselist3)//2):
    reverselist3[i],reverselist3[len(reverselist3)-i-1] = reverselist3[len(reverselist3)-i-1], reverselist3[i]
    print(f"the reversed list at i={i} is {reverselist3} \n")

print(f"The reversed list using swapping variables is {reverselist3} \n")
if reverselist1==reverselist2 and reverselist2==reverselist3:
    print("All gives same answer \n")
