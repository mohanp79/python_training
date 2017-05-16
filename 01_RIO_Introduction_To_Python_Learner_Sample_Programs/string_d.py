def mix_up(a, b):
  a_swapped = b[:2] + a[2:]
  print("The Characters before the 2nd letter in the string 'b' is: ",b[:2])
  print("The Characters From the 2nd letter in the string 'a' is: ",a[2:])
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped

#EX: Run this program like mix_up('dog', 'dinner')
