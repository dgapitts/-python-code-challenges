## is_palidrome


> A palindrome is a word or phrase that reads the same forwards as it does backwards... 
> Your function should only consider letters, A through Z, when evaluating the string and you should ignore their case, treating uppercase and lowercase letters as being the same. 


### Step01 - Base functionality 

* basic tests below show this is working
* I will also need to remove white space, punctation and make case insensitve
* it can be made more efficient (exit when first False found)


```
~/projects/python-code-challenges $ cat docs/is_palidrome.py
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
```
and 
```
~/projects/python-code-challenges $ /usr/local/opt/python@3.9/bin/python3.9 /Users/dave/projects/python-code-challenges/docs/is_palidrome.py
12321
round: 0
0,4
1,1
round: 1
1,3
2,2
round: 2
2,2
3,3
12321 True
~/projects/python-code-challenges $ /usr/local/opt/python@3.9/bin/python3.9 /Users/dave/projects/python-code-challenges/docs/is_palidrome.py
1232
round: 0
0,3
1,2
0 False
round: 1
1,2
2,3
1 False
round: 2
2,1
3,2
2 False
1232 False
~/projects/python-code-challenges $ /usr/local/opt/python@3.9/bin/python3.9 /Users/dave/projects/python-code-challenges/docs/is_palidrome.py
1232
round: 0
0,3
1,2
0 False
round: 1
1,2
2,3
1 False
round: 2
2,1
3,2
2 False
1232 False
~/projects/python-code-challenges $ /usr/local/opt/python@3.9/bin/python3.9 /Users/dave/projects/python-code-challenges/docs/is_palidrome.py
123321
round: 0
0,5
1,1
round: 1
1,4
2,2
round: 2
2,3
3,3
123321 True
~/projects/python-code-challenges $ 
```
