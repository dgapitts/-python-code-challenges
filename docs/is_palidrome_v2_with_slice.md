## is_palidrome - v2 "with slice" - signficantly more efficient

Following on from my "brute force approach" [here](/is_palidrome-base-functionality.md):
* we can simply this with a slice operation
* the key step/logic is now `test_reversed=test[::-1]`


```
~/projects/python-code-challenges $ cat docs/is_palidrome_v2_with_slice.py
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
```

for example:

```
~/projects/python-code-challenges $ python3 docs/is_palidrome_v2_with_slice.py
123321:123321
12 3 32 1: True
```