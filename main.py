number=int(input('Enter a number'))
digits=len(str(number))
result=0
temp=number
while temp>0:
    digit=temp%10
    result+=digit**digits
    temp//=10
if number==result:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')        