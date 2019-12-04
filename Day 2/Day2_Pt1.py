#Advent of Code 2019 Day 2 Part 1: 1202 Program Alarm

def alarm(filepath):
    with open(filepath) as intcode:
        intcode = list(map(int, intcode.read().split(',')))
        
        intcode[1] = 12
        intcode[2] = 2
    
        for x in [intcode[i:i + 4] for i in range(0, len(intcode), 4)]:
            if x[0] == 99:
                break
            else:
                if x[0] == 1:
                    intcode[x[3]] = intcode[x[1]] + intcode[x[2]]
                else:
                    intcode[x[3]] = intcode[x[1]] * intcode[x[2]]

    return(intcode[0])

print(alarm('Day2.txt'))