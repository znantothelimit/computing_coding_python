#20190954 허진환 조건문

'''
a =90

if(a>=90):
    print("합격입니다")

a = int(input("점수를 입력하세요 : "))

if(a>=90):
    print("합격입니다")
else:
    print("불합격입니다")
'''
    
'''
여러 줄 주석처리
'''

'''
num1 = int(input("1st 숫자를 입력하세요(정수) : "))
num2 = int(input("2nd 숫자를 입력하세요(정수) : "))
op = input("+, -, *, / 중 연산자를 선택하시오(문자) : ")

if(op == "+"):
    print("두 수의 합 = ", num1+num2)
if(op == "-"):
    print("두 수의 차 = ", num1-num2)
if(op == "*"):
    print("두 수의 곱 = ", num1*num2)
if(op == "/"):
    print("두 수의 나누기 = ", num1/num2)
else:
    print("사칙 연산자만 사용해주십시오.")
'''

'''
a = int(input("점수를 입력하시오(정수) : "))
if(a>=90):
    print("A학점입니다.")
else:
    if(a>=80):
        print("B학점입니다.")
    else:
        if(a>=70):
            print("C학점입니다.")
        else:
            if(a>=60):
                print("D학점입니다.")
            else:
                print("F학점입니다.")
'''             

'''
import random
a = random.randint(1, 100)
if(a%2==0):
    print("a는 짝수입니다.")
else:
    print("a는 홀수입니다.")
print("a값 = ", a)
'''

'''
a = int(input("점수를 입력하시오(정수) : "))
if(a>=90):
    print("A학점입니다.")
elif(a>=80):
    print("B학점입니다.")
elif(a>=70):
    print("C학점입니다.")
elif(a>=60):
    print("D학점입니다.")
else:
    print("F학점입니다.")
'''

# 속도 입력받아 속도가 40미만이면 저속 40이상 80미만이면 정상속도 80이상이면 고속 출력
speed = int(input("속도를 입력하시오 : "))
if(speed < 40):
    print("저속")
elif(speed < 80):
    print("정상")
else:
    print("고속")
