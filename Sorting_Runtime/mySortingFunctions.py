# Name: Christina Nguyen

#
# By submitting this file as my own work, I declare that this
# code has been written on my own with no unauthorized help. I agree to the
# CU Honor Code. I am also aware that plagiarizing code may result in
# a failing grade for this class.
from __future__ import print_function
import sys
import random
import time


# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort

    n = len(lst)
    if (n > 1):
    	q = n/2
    	lst[:q] = mergeSort(lst[:q])
    	lst[q:] = mergeSort(lst[q:])
    	merge(lst, q, n)
    #print(lst)
    return lst # TODO: change this
    
def merge(lst, q, n):
	lstHalf1 = lst[:q]
	lstHalf2 = lst[q:]
	firstLen = len(lstHalf1)
	secondLen = len(lstHalf2)
	i = 0
	j = 0
	k = 0
	#print(lstHalf1, lstHalf2, n)
	while (i < firstLen and j < secondLen):
		if (lstHalf1[i] <= lstHalf2[j]):
			lst[k] = lstHalf1[i]
			i = i+1
			k = k + 1
		else: 
			lst[k] = lstHalf2[j]
			j = j + 1
			k = k + 1
	while (i < firstLen):
		lst[k] = lstHalf1[i]
		i = i + 1
		k = k + 1
	while (j < secondLen):
		lst[k] = lstHalf2[j]
		j = j + 1
		k = k + 1
	#print(lst)
	return lst

#------ Quick Sort --------------
def quickSort(lst, s=0, n=-10):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
	if (n == -10):
		n = len(lst)
	if (s < n):
		q = partition(lst, s, n)
		quickSort(lst, s, q)
		quickSort(lst, q+1, n)
	#print(lst)
	return lst # TODO: change this
    
def partition(lst, s, n):
	r = random.randint(s, n-1)
	#print(r)
	lst[n-1], lst[r] = lst[r], lst[n-1]
	pivot = lst[n-1]
	i = s-1
	for k in range(s, n-1):
		if lst[k] <= pivot:
			i = i + 1
			lst[k], lst[i] = lst[i], lst[k]
	lst[i+1], lst[n-1] = lst[n-1], lst[i+1]
	#print(i+1)
	#print(lst)
	return i+1
    


# ------ Timing Utility Functions ---------

# Code below is given only for demonstration purposes

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity for your sorting routines.
def avgSortingRunTimes():
	for i in range(5, 501, 5):
		isTime = 0;
		msTime = 0;
		qsTime = 0;
		for k in range(0,20*i):
			lst = generateRandomList(i)
			isTime = isTime + measureRunningTimeComplexity(insertionSort,lst)
			msTime = msTime + measureRunningTimeComplexity(mergeSort,lst)
			qsTime = qsTime + measureRunningTimeComplexity(quickSort,lst)
		avgIS = isTime / (20*i)
		avgMS = msTime / (20*i)
		avgQS = qsTime / (20*i)
		print(i, ",", avgIS, ",", avgMS, ",", avgQS)
		
def worstRunTimes():
	for i in range(5, 501, 5):
		isTime = 0;
		msTime = 0;
		qsTime = 0;
		temp = 0;
		for k in range(0, 20*i):
			lst = generateRandomList(i)
			temp = measureRunningTimeComplexity(insertionSort,lst)
			if (temp > isTime):
				isTime = temp
			temp = measureRunningTimeComplexity(mergeSort,lst)
			if (temp > msTime):
				msTime = temp
			temp = measureRunningTimeComplexity(quickSort,lst)
			if (temp > qsTime):
				qsTime = temp
		print(i, ",", isTime, ",", msTime, ",", qsTime)
			
#mergeSort([1,2,3,16,-53,4,2,9,7])
#quickSort([7,-12,15,32,-4,3,5,4,2])
#avgSortingRunTimes()
#worstRunTimes()
