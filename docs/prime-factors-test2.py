start_num=11
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

