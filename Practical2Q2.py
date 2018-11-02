# Given weightages are represented as below and are universal
MIDSUMMERTEST = 0.20
ASSIGNMENT1 = 0.25
ASSIGNMENT2 = 0.35
GENERALPERFORMANCE = 0.20

# User input of scores
gradeMidSummerTest = int(input("Enter your Midsummer test scores"))
gradeAssignment1 = int(input("Enter your Assignemt1 test scores"))
gradeAssignment2 = int(input("Enter your Assignemt2 test scores"))
gradeGeneralPerformance = int(input("Enter your General Performance scores"))

# Calculate weighted average
weightSummer = (gradeMidSummerTest/100)*MIDSUMMERTEST
weightAssign1 = (gradeAssignment1/100)*ASSIGNMENT1
weightAssign2 = (gradeAssignment2/100)*ASSIGNMENT2
weightGeneral = (gradeGeneralPerformance/100)*GENERALPERFORMANCE


# Call function to calculate the weighted average

def sumAvgWeight():
    return ((weightSummer+weightAssign1+weightAssign2+weightGeneral)*100)


print(sumAvgWeight())
