print('input a positive number: ')
num = int(input())
while(num<=0):
    print('the input number is nonpositive, please input again')
    num = int(input())

def judge(num):
    if(num%2==0 & num%3==0 & num%4==0):
        print('the number ' , num , ' is multiple of 2,3,4')
    else:
        print('the number ' , num , ' is not a multiple of 2,3,4')

judge(num)
print('------------------------------------------------\nEnd of program')
exit()