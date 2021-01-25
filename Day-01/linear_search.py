""""This demonstrates the Linear Search algorithm in Python."""
import time

print("#####Demonstration of Linear Search.#####")
print("Enter how many elements to be stored in the list.")
noOfElements = int(input()) # Enter the no of Elements
print("Enter the elements in the list.")
inputElements = [] # List of input elements
for _ in range(noOfElements):
    number = int(input()) 
    inputElements.append(number)

print("Enter the key to be searched.")
key = int(input())

startTime = time.time()

for i in range(len(inputElements)):
    if key == inputElements[i]:
        print("Found {} at the index {}".format(key,i+1))
    elif key != inputElements[i]:
        pass

endTime = time.time()
totalTime = endTime - startTime
print("Total time taken. {:.3f} seconds".format(totalTime * 60 ))