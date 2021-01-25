"""This demonstrates the maximum sum of all possible subarrays from a list."""
import time

print("#####Demonstration of Max sum of Subarray Generation.#####")
print("Enter how many elements to be stored in the list.")
noOfElements = int(input()) # Enter the no of Elements
print("Enter the elements in the list.")
inputElements = [] # List of input elements
for _ in range(noOfElements):        
    number = int(input()) 
    inputElements.append(number)
                  
sumSubarrays = []

for i in range(len(inputElements)):
    for j in range(len(inputElements)):
        subarray = inputElements[i:j]
        sumSubarrays.append(sum(subarray))

print("Maximum sum among subarrays is: {}".format(max(sumSubarrays)))


