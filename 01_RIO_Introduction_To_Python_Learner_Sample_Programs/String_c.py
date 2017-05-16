def fix_start(s):
  
  front = s[1]
  print ("Front value is:",front)
  back = s[1:]
  print ("Back value is:",back)
  fixed_back = back.replace(front, 'x')
  return front +" " + fixed_back

  #RUn this program like this fix_start('Google is good')
