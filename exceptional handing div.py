try: 
  x=int(input("Enter x value")) 
  y=int(input("Enter x value")) 
  z=x/y 
except ZeroDivisionError: 
  print("except ZeroDivisionError block") 
  print("Division by 0 not accepted") 
except: 
  print('Some error occurred.') 
else: 
  print("Division = ", z) 
finally: 
  print("Executing finally block") 
  x=0 
  y=0 
print ("Out of try, except, else and finally blocks.")
