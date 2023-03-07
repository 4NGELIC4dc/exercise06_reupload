theSum=0.0
theAverage=0.0
theDivision=0.0
name=int(input("Enter a number or press enter to quit: "))
while name != "":
    theSum += float(name)
    theDivision += 1
    name=input("Enter a number or press enter to quit: ")
theAverage=theSum/theDivision
print("The sum is:", theSum)
print("The average is:", theAverage)
