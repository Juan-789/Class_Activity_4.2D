"""
Write a program that takes from the user a number A and B (A ≤ B). Print every second number from A to B inclusively horizontally in ascending order.
"""
numA = int(input("Starting number? "))
numB = int(input("Limiting number? "))
for i in range(numA,numB + 2,2):
  print (i, end = " ")
#iterates every number between numA and numB with a step of 2