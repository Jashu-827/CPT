# -*- coding: utf-8 -*-
"""CPT_03/07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t7UUnTAty6CcrpMBOrrWvm5Dvp3tA0bY
"""

'''searching
used for any searching element in a large data
iii. Jump search
1. size n/ sorted
2. create a block key
3. search operation will be performed arr[m]< var/key <arr(k+1)[m]
4. compare each jump linearly
Time Complexity - O(sqrt(n))
space Complexity - 1
'''

import math

def jump_search(arr, target):
  if not arr:
    return -1
  n=len(arr)
  step=int(math.sqrt(n))
  # print(step)
  prev=0
  while prev < n and arr[prev]<target:
    prev += step
    # print(prev)
  for i in range(max(0, prev-step), min(n, prev+1)):
    # print(prev-step,"   ",prev+1 )
    if arr[i]==target:
      return i
  return -1

arr=[1,5,7,8,9,11]
target= 7
result= jump_search(arr, target)
print(f"Element {target} foud at {result}")

''' EXPOnential SEARCH
1. sorted numbers searching
2. check the array != 0
3. check the first element
4. find the range using exponential
while for boundary
identify within boundary
5. range perform binary search
6. return result '''

def bsearch_range(arr, target, left, right):
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]<target:
      left =mid+1
    else:
      right=mid-1
  return -1
def expo_search(arr, target):
  if not arr:
    return -1
  if arr[0]==target:
    return 0
  n=len(arr)
  i=1
  while i<n and arr[i]<=target:
    i*=2
  return bsearch_range(arr, target, i//2, min(i, n-1))
arr= [2,4,6,8,10,12,14]
target = 10
result = expo_search(arr, target)
print(f"Element {target} found at index: {result}")

'''FIBONACCI SEARCH
1.
'''

# from re import I
def fibsearch(arr, target):
  if not arr:
    return -1
  n=len(arr)
  fib2=0
  fib1=1
  fib=fib1+fib2
  while fib <n:
    fib2=fib1
    fib1=fib
    fib= fib1+fib2
  offset=-1
  while fib>1:
    i=min(offset + fib2, n-1)
    if arr[i]==target:
      return i
    elif arr[i]<target:
      offset=i
      fib=fib1
      fib1=fib2
      fib2=fib-fib1
    else:
      fib=fib2
      fib1=fib1-fib2
      fib2=fib-fib1
  if fib1 and arr[offset+1]==target:
    return offset+1
  return -1
arr=[1,3,5,7,9,11]
target=7
result=fibsearch(arr, target)
print(f"Element {target} found at index {result}")

