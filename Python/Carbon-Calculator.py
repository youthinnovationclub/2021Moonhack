#!/bin/python3
from data import questions
  
total = 0
for question in questions:
  print(question['question'])
  i = 0
  for answer in question['answers']:
    print(str(i) + " " + answer['answer'])
    i += 1
  
  valid = False
  while not valid:
    response = input("Enter your answer (0-" + str(i-1) + ")")
    
    if response.isdigit():
      response = int(response)
    else:
      print("That's not a number!")
      
    if response >= 0 and response < i:
      valid = True
    else:
      print("Please enter a number between 0 and " + str(i-1))
      
  total += question['answers'][response]['carbon']

print("You emit approximately " + str(total) + "kg of CO2 per year.")