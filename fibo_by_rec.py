
def fibo_rec(a):
  if a==1:
   return 1
  if a==0: 
    return 0; 
  else: return fibo_rec(a-1)+fibo_rec(a-2)  

a=int(input("Enter a number:"))
for i in range(0,a+1): 
    print(i,':',fibo_rec(i))