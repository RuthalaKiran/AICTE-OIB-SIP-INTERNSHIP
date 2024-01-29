weight = float(input("enter your weight in kgs :"))
height = float(input("enter your height in cm  :"))

meter = height/100

bmi = weight/meter**2

print("your bmi is",bmi)
if bmi < 18.5 :
    print("under weight")
elif bmi < 25 :
    print("healthy")
else:
    print("over weight")

