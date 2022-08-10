import re
def is_palidrome (test):
  test=re.sub('[^A-Za-z0-9]+', '',test).lower()
  for i in range(0,round((len(test)-1)/2)+1):
    if test[i] != test[(len(test)-1)-i]:
      return False
  return True

#input_str="1'2!3?4321"
#input_str="1232"
#input_str="12320"
input_str="12 3 32 1"
print(str(input_str)+": "+str(is_palidrome(input_str)))



  
