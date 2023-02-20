def partition(arr,left,right):
  i=left+1
  pivot=arr[left]
  for j in range(left+1,right+1):
    if arr[j]<pivot:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
  pos=i-1
  arr[left],arr[pos]=arr[pos],arr[left]
  return pos
  
def quicksort(arr,left,right):
  if left<right:
    pivot=partition(arr,left,right)
    quicksort(arr,left,pivot-1)
    quicksort(arr,pivot+1,right)
    
n=int(input("Enter length of array: "))
print("Enter elements: ")
arr={}
for i in range(0,n):
  arr[i]=int(input())
quicksort(arr,0,n-1)
print("Sorted array: ")
for i in range(n):
  print(arr[i])