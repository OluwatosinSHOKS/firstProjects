print('Weight Converter App')

print("Hi!")

inputWeight = float(input("Enter your weight? "))

myWeightInKg = float(inputWeight / float(2.2046))
myNewWeightInKg = str(myWeightInKg)

myWeightInlbs = float(inputWeight * float(2.2046))
myNewWeightInlbs = str(myWeightInlbs)

weightUnit = str(input('Is your inputed weight in (K)g or (L)bs? '))

#print("Your weight is " + str(inputWeight))
#print("Your weight is " + myNewWeightInKg)
#print("Your weight is " + myNewWeightInlbs)

if weightUnit.upper() == "L":
    print("Your weight is " + myNewWeightInKg + " kg")
elif weightUnit.upper() == "K":
    print("Your weight is " + myNewWeightInlbs + " lbs")
else:
    print("Invalid weight Unit!")

print("Thank you!!")
