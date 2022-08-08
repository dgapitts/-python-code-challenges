import re
test="1'2!3?21"
#test="1232"
#test="12320"
test="12 3 32 1"
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
test=re.sub('[^A-Za-z0-9]+', '',test).lower()
print(test)
is_palidrome=True
for i in range(0,round((len(test)-1)/2)+1):
  print(str("round: ")+str(i))
  print(str(i)+","+str((len(test)-1)-i))
  print(test[i]+","+test[(len(test)-1)-i])
  if test[i] != test[(len(test)-1)-i]:
    is_palidrome=False
    print(str(i) + " False")


print (test + " " + str(is_palidrome))

  
