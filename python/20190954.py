a=10
print("a값은: ", a)
b=20
print("b값은: ", b)

print("두 수의 합은: ", a+b)
print("#1", a,"(a값) +", b, "(b값) =", a+b, "입니다")
print("#2", "%d (a값) + %d (b값) = %d 입니다" %(a, b, a+b))
print("#3 %.1f (a값;실수) + %.1f (b값;실수) = %f 입니다" %(a, b, a+b))


val_1 = "10.925"
val_2 = float(val_1)
val_3 = int(val_2)
val_4 = str(val_3)
print(val_1, val_2, val_3, val_4)

###오류발생
###문자열->실수로 바꿔준 다음 int로 바꿔야 동작함
#val_1 = "10.925"
#val_3 = int(val_1) 
val_1 = "10"
val_3 = int(val_1)
print(val_1, val_3)

#1
a=int(input("a값 입력(정수): "))
b=int(input("b값 입력(정수): "))
print("#1", a,"(a값) +", b, "(b값) =", a+b, "입니다")
print("#2", "%d (a값) + %d (b값) = %d 입니다" %(a, b, a+b))

#2
a=int(input("a값 입력(정수): "))
b=int(input("b값 입력(정수): "))
print("#1", a,"(a값) +", b, "(b값) =", a+b, "입니다")
print("#2", "%d (a값) + %d (b값) = %d 입니다" %(a, b, a+b))

#3
a=int(input("a값 입력(정수): "))
b=int(input("b값 입력(정수): "))
print("#1", a,"(a값) +", b, "(b값) =", a+b, "입니다")
print("#2", "%d (a값) + %d (b값) = %d 입니다" %(a, b, a+b))
