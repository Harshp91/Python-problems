print("Enter 10 Numbers: ")
arr = []
for i in range(10):
  arr.insert(i, int(input()))
print("Enter the Number to Search: ")
num = int(input())
for i in range(10):
  if num==arr[i]:
    index = i
    break
print("\nNumber Found at Index Number: ")
print(index)