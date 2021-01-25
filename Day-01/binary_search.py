""""This demonstrates the Binary Search algorithm in Python."""

# This is Binary search function that outputs -1 or element index.
def BinarySearch(listElements,key):
    end = len(listElements)
    start = 0
    while (start<=end):
        mid = (end + start) // 2

        if listElements[mid] == key:
            return mid
        elif listElements[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print("#####Demonstration of Binary Search.#####")
print("Enter how many elements to be stored in the list.")
noOfElements = int(input()) # Enter the no of Elements
print("Enter the elements in the list.")
inputElements = [] # List of input elements
for _ in range(noOfElements):
    number = int(input()) 
    inputElements.append(number)

print("Enter the key to be searched.")
key = int(input())

midIndex = BinarySearch(inputElements,key)

if midIndex != -1:
    print("Found {} at {}".format(key,midIndex+1))
else:
    print("{} not FOund in the input list".format(key))
