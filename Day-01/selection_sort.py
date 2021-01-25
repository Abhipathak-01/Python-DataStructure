""""This demonstrates the Selection Sort algorithm in Python."""
import time

def AscendingSelectionSort(elementList):
    """This implements ascending selection sort."""
    
    for i in range(len(elementList)):
        minimum_index = i
        for j in range(i+1, len(elementList)):
            if elementList[minimum_index] > elementList[j]:
                minimum_index = j
        elementList[i],elementList[minimum_index] = elementList[minimum_index], elementList[i]


def DescendingSelectionSort(elementList):
    """This implements descending selection sort."""
    
    for i in range(len(elementList)):
        minimum_index = i
        for j in range(i+1, len(elementList)):
            if elementList[minimum_index] < elementList[j]:
                minimum_index = j
        elementList[i],elementList[minimum_index] = elementList[minimum_index], elementList[i]


print("#####Demonstration of Selection Sort.#####")
print("Enter how many elements to be stored in the list.")
noOfElements = int(input()) # Enter the no of Elements
print("Enter the choice for sorting.")
choice = input()
print("Enter the elements in the list.")
inputElements = [] # List of input elements
for _ in range(noOfElements):
    number = int(input()) 
    inputElements.append(number)

if choice == "ascending":
    print("Element List before sorting.")
    startTime = time.time()
    print(inputElements)
    AscendingSelectionSort(inputElements)
    print("Element List After sorting in Ascending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60 ))
elif choice == "descending":
    print("Element List before sorting.")
    startTime = time.time()
    print(inputElements)
    DescendingSelectionSort(inputElements)
    print("Element List After sorting in Descending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60))
else:
    print("Enter valid choice.")