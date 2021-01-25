""""This demonstrates the insertion Sort algorithm in Python."""
import time

def AscendingInsertionSort(elementList):
    for i in range(1,len(elementList)):
        key = elementList[i]

        j = i-1
        while j >= 0 and key < elementList[j]:
            elementList[j + 1] = elementList[j]
            j = j-1
        elementList[j + 1] = key


def DescendingInsertionSort(elementList):
    for i in range(1,len(elementList)):
        key = elementList[i]
        j = i-1
        while j >= 0 and key > elementList[j]:
            elementList[j + 1] = elementList[j]
            j = j-1
        elementList[j + 1] = key

print("#####Demonstration of Insertion Sort.#####")
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
    AscendingInsertionSort(inputElements)
    print("Element List After sorting in Ascending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60 ))
elif choice == "descending":
    print("Element List before sorting.")
    startTime = time.time()
    print(inputElements)
    DescendingInsertionSort(inputElements)
    print("Element List After sorting in Descending order.")
    print(inputElements)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Total time taken. {:.3f} seconds".format(totalTime * 60))
else:
    print("Enter valid choice.")