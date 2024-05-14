ans = 'y'
while ans.lower() == 'y':
    print("---------------------------------------")
    print("&&&  WELCOME TO THE BMI CALCULATOR  &&&")
    print("---------------------------------------")
    weight = int(input("Enter the weight in kg : "))
    height = int(input("Enter the height in cm : ")) / 100
    bmi = weight / height ** 2
    print("Calculated BMI = {:.2f}".format(bmi))
    if bmi < 18.5:
        print("Underweight !!")
    elif bmi < 25:
        print("Normal Weight !!")
    elif bmi < 30:
        print("Overweight !!")
    else:
        print("Obesity !!")
    print("---------------------------------------")
    print()
    ans = input("Press 'y/Y' to run the BMI calculator again : ")
    print()