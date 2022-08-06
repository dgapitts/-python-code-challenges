#test="12321"
#test="1232"
#test="12320"
test="123321"

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

  
