#Advent of Code 2019 Day 1 Part 1: The Tyranny of the Rocket Equation
fuelReq = []
def fuelCalc(mass):
    mass = int(mass)
    return mass//3-2

filepath = 'Day1.txt'
with open (filepath) as masses:
    for mass in masses:
        fuelReq.append(fuelCalc(mass))
print(sum(fuelReq))