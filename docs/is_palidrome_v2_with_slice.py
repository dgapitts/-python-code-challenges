import re
def is_palidrome (test):
  test=re.sub('[^A-Za-z0-9]+', '',test).lower()
  test_reversed=test[::-1]
  print (test + ":" + test_reversed)
  if test_reversed == test:
    return True
  else:
    return False
  

#input_str="1'2!3?4321"
#input_str="1232"
#input_str="12320"
input_str="12 3 32 1"
print(str(input_str)+": "+str(is_palidrome(input_str)))



  
