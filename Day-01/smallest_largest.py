""" This demonstrates the smallest and largest number in Python. """

print("#####Demonstration of Search of smallest and largest number.#####")
print("Enter how many elements to be stored in the list.")
noOfElements = int(input()) # Enter the no of Elements
print("Enter the elements in the list.")
inputElements = [] # List of input elements
for _ in range(noOfElements):
    number = int(input()) 
    inputElements.append(number)

minNumber = inputElements[0]
for i in range(len(inputElements)): 
    if minNumber > inputElements[i]:
        minNumber = inputElements[i]
    else:
        pass

maxNumber = inputElements[0]
for i in range(len(inputElements)): 
    if maxNumber < inputElements[i]:
        maxNumber = inputElements[i]
    else:
        pass

print("Smallest number from the list is {}".format(minNumber))
print("Largest number from the list is {}".format(maxNumber))

