L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List: ", L)

#Variable to store the sum of
#The list
count = 0

#Finding the sum
for i in L:
    count += i

#Divide the total elements by
#Number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

#Sorting the elements of the list
L.sort()

#Printing the first element
print("Smallest element is: ", L[0])

#Printing the largest element
print("The largest element is: ", L[-1])