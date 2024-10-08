import array as arr 

#original array
numbers = arr.array('i',[10,20,30])
print('Before',numbers)
#add the integer 40 to the end of numbers
numbers.append(40)
print('After',numbers)
#output
#array('i', [10, 20, 30, 40])
