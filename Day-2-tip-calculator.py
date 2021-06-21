print("Wellcome to the tip Calculator :")

#collecting billing info

bill = float(input("What was the total bill ? = $"))
tip = int(input("What persentage of tip whould you like to give, 10, 12 or 15% = "))
people = int(input("How many people to split the bill? = "))

# calculating bill for each person

bill_final=(bill+tip)/people

# printing billing detail

print(f"Each person should pay : {bill_final}")
input()