## Prime Factors - First Draft Solution - brutal, inelegant but works

My solution below works and is fast for smaller number (below 10K) but gets very slow for larger numbers.

So 7/10 for getting the right answer but 
* this is a brute force method and there must be a better iterative method
* the code is not elegant - the final if check appears supurflous  (i.e. I wouldn't need the final if statement, if I had to rememberd to increment my upper bound by one - something to remember for the next solution)


### First Draft Solution - test01 

```
~/projects/python-code-challenges $ cat docs/prime-factors-test1.py
start_num=10
leftover=start_num
prime_factors = []
for i in range(2,start_num):
    check_again_flag=True
    while check_again_flag==True:
        remainder_test = (leftover%i)
        if remainder_test == 0:
          prime_factors.append(i)
          leftover=leftover/i
          #print("leftover : "+str(i))
        else:
          check_again_flag=False
               
if leftover>1:
   prime_factors.append(leftover)

print(prime_factors)
```
and it is both fast and right
```
~/projects/python-code-challenges $ time python3 docs/prime-factors-test1.py
[2, 5]

real	0m0.134s
user	0m0.044s
sys	0m0.027s
```
although stepping through the visualizer I can see a code improvement:


 (i.e. I wouldn't need the final if statement, if I had to rememberd to increment my upper bound by one - something to remember for the next solution)



### First Draft Solution - test02

Really this ought to be parameterized
```
~/projects/python-code-challenges $ diff docs/prime-factors-test1.py docs/prime-factors-test2.py
1c1
< start_num=10
---
> start_num=11
```
but it works and is still fast
```
~/projects/python-code-challenges $ time python3 docs/prime-factors-test2.py
[11]

real	0m0.183s
user	0m0.062s
sys	0m0.038s
```

### First Draft Solution - test03


Again really ought to be parameterized but it works and is still fast
```
~/projects/python-code-challenges $ diff docs/prime-factors-test1.py docs/prime-factors-test3.py
1c1
< start_num=10
---
> start_num=630
```
...
```
~/projects/python-code-challenges $ time python3 docs/prime-factors-test3.py
[2, 3, 3, 5, 7]

real	0m0.109s
user	0m0.046s
sys	0m0.028s
```

### First Draft Solution - test04


Hmm no longer fast but the results are correct
```
~/projects/python-code-challenges $ diff docs/prime-factors-test1.py docs/prime-factors-test4.py
1c1
< start_num=10
---
> start_num=111191111
```
...
```
~/projects/python-code-challenges $ time python3 docs/prime-factors-test4.py
[111191111]

real	0m44.791s
user	0m44.477s
sys	0m0.095s
```

### First Draft Solution - test05


Again no longer fast but the results are correct (not hundred percent sure if 358681 is prime but the algorithm "looks good" ... if inefficent for larger numbers)
```
~/projects/python-code-challenges $ diff docs/prime-factors-test1.py docs/prime-factors-test5.py
1c1
< start_num=10
---
> start_num=111191110
```
...
```
~/projects/python-code-challenges $ time python3 docs/prime-factors-test5.py
[2, 5, 31, 358681]

real	0m41.981s
user	0m41.807s
sys	0m0.076s
~/projects/python-code-challenges $ echo '2*5*31*358681'|bc
111191110
```







