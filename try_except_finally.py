#Example 1
try:
  x = 'Doing something'

except:
  print('Something wrong happend')

finally:
  y = 'Always will execute this line'


#Example 2
try:
  x = 'Doing something'

except Exception as e:
  print(e) #Error message

finally:
  y = 'Always will execute this line'
