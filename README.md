# Python Implementation for Data structures and algorithms

## Day-01

Today we are going to see the implementation and understanding of following concepts and techniques.
1. Linear Search
2. Binary Search
3. Insertion Sort
4. Bubble Sort
5. Selection Sort
6. Generating subarrays
7. max sum of all possible subarrays
8. smallest and greatest element of the given array
   
    1. ### Linear Search
            
**Definition**:-

linear search or sequential search is a method for finding an element within a list. It sequentially check each element of the list unitl a match is found or the whole list has been searched. [wikipedia]

**Steps**:-
Given an array as an input and a key to be searched in the array.

1. Start from the leftmost element of the given array and one by one compare the (key) with each element of the array.
2. if (key) matches with an element, return the index
3. if (key) doesn't match with any of elements, return -1

**Analysis**:-

Linear seach is rarely used practically because other algorithms such as the binary search algorithm and hash tables allows significantly faster-searching comparisons to Linear search. 

The time complexity of the above algorithm is O(N).