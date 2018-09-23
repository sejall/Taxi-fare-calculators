#two inputs asking for the distance and passengers
km = float(input("Enter the distance of the taxi ride in kilometres (KM): "))
passengers = int(input("Enter the number of passengers: "))
#calculation to work out the cost
cost = 3 + ((km-1)*2)
#checks to see if the number of passengers is more than 5 so that the additional 50% cost can be added
if passengers > 5:
	#calculates the extra cost if the condition is true
    cost = cost * 1.5
#displays the total cost of the journey
print("The total cost of the journey for",passengers,"passengers is £{:.2f}".format(cost))
