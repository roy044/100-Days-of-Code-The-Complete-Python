
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


weight_as_int = int(weight)
height_as_float = float(height)


bmi = weight_as_int / height_as_float**2

bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
