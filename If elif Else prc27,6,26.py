# Str="Arfa is a brilant student.\nMy Collige."
# print(Str.replace("Collige","University"))

# Apna="MY$ Collige$ $909.9" 
# print(Apna.count("$"))

# light="Pink"

# if(light == "Red"):
#     print("Stop")
# elif(light == "Green"):
#     print("Run")
# elif(light == "Yello"):
#     print("See")
# else:
#     print("lighr id broken")






print("end of code")

marks = int (input("enter students marks :"))

if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <90):
    grade = "B"
elif(marks >=70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("grade of the students ->",grade)
