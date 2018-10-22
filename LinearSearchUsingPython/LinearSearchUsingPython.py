def linearsearch(list,n):
    found = 0
    for i in range(len(list)):
        if list[i]==n:
            print("Element found at {} position".format(i+1))
            found = 1
            return True
  
    if found !=0:
        print("Element {} not found".format(n))
        return True
    return

list = []

size = int(input("Enter the size of the array: "))

for i in range(size):
    x =  int(input("Enter the element at {} position: ".format(i+1)))
    list.append(x)

print("Entered array list is:")
for lists in list:
    print(lists,end="\t")

se = int(input("\nEnter the array element to be searched: "))
linearsearch(list,se)

