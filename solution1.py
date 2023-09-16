def count_down(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down(n-1)
   
#test case
n=8
count_down(n)

