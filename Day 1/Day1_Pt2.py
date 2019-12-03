#Advent of Code 2019 Day 1 Part 2: The Tyranny of the Rocket Equation
fuelReq = []
def fuelCalc(mass):
    mass = int(mass)
    return mass//3-2

filepath = 'Day1.txt'
with open (filepath) as masses:
    for mass in masses:
        fuel = fuelCalc(mass)
        fuelTotal = fuel
        while fuel > 0:
            fuel = fuelCalc(fuel)
            if fuel > 0:
                fuelTotal += fuel
        
        fuelReq.append(fuelTotal)
print(sum(fuelReq))