equations = [list(e.split(": ")) for e in open("puzzle.txt").read().splitlines()]

total = 0


def check(operands, result):
    def calc(new_index, res):
        if new_index == len(operands):
            return res == result

        next_operand = operands[new_index]
        
        addition = calc(new_index + 1, res + next_operand)
        multiply = calc(new_index + 1, res * next_operand)
        concatenation = calc(new_index + 1, int(f"{res}{next_operand}"))

        return addition or multiply or concatenation

    return calc(1, operands[0])


for equation in equations:
    result = int(equation[0])
    operands = list(int(n) for n in equation[1].split())
    
    if check(operands, result):
        total += result
        

print(total)