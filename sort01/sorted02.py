new_list=[]

for data in open("sort.txt"):
    new_list.append(data.strip())
    
print("This is our list", new_list)
print()
print("This is our list sorted with the sorted function:", sorted(new_list))


print()
print()

sortedlist=sorted(new_list)


print()
print("Another sorted list:" + str(sortedlist))






    


            


    
