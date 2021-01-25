""""This demonstrates the insertion Sort algorithm in Python."""
import time


def AscendingBubbleSort(elementList):
    """ This function implments the bubble sort in ascending sort."""
    end = len(elementList)

    for i in range(end):
        for j in range(0, end-i-1):
            if elementList[j] > elementList[j+1]:
                elementList[j], elementList[j+1] = elementList[j+1], elementList[j]

def DescendingBubbleSort(elementList):
    """This function implments bubble sort in descending sort."""
    end = len(elementList)

    for i in range(end):
        for j in range(0, end-i-1):
            if elementList[j] < elementList[j+1]:
                elementList[j], elementList[j+1] = elementList[j+1], elementList[j]


print("#####Demonstration of Bubble Sort.#####")
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
    AscendingBubbleSort(inputElements)
    print("Element List After sorting in Ascending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60 ))
elif choice == "descending":
    print("Element List before sorting.")
    startTime = time.time()
    print(inputElements)
    DescendingBubbleSort(inputElements)
    print("Element List After sorting in Descending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60))
else:
    print("Enter valid choice.")