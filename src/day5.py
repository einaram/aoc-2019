
def get_input_values(param_value, data_op, i):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    try:
        if param_value == POSITION_MODE:
            num = data_op[data_op[i+1]]

        elif param_value == IMMEDIATE_MODE:
            num = data_op[i+1]

        return int(num)
    except:
        return None  # skipp num2-3-4 if not existing


def opcode_runned(data_runner, o_input=None):
    data_op = data_runner.copy()
    print("runner")

    ADD = 1
    MULTIPL = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8

    i = 0
    iters = 0
    while iters < 500:
        iters += 1
        if int(data_op[i]) == 99:
            break

        def parse_opcode(raw_opcode):
            full_opcode = str(raw_opcode).zfill(5)
            param_mode1 = int(full_opcode[-3])
            param_mode2 = int(full_opcode[-4])
            param_mode3 = int(full_opcode[-5])
            opcode = int(full_opcode[-2:])
            return param_mode1, param_mode2, param_mode3, opcode
        param_mode1, param_mode2, param_mode3, opcode = parse_opcode(
            data_op[i])

        i_output = data_op[i+3]

        num1 = get_input_values(param_mode1, data_op, i)
        num2 = get_input_values(param_mode2, data_op, i+1)
        num3 = get_input_values(param_mode3, data_op, i+2)

        if opcode in [ADD, MULTIPL]:
            if opcode == 1:
                def opfunc(x, y): return x+y
            elif opcode == 2:
                def opfunc(x, y): return x*y

            data_op[i_output] = opfunc(num1, num2)
            new_i = i + 4
        elif opcode in [INPUT, OUTPUT]:
            if opcode == INPUT:
                data_op[data_op[i+1]] = int(o_input)
                int(o_input)  # validation-light
            elif opcode == OUTPUT:
                
                if num1 != 0:  # WTF?
                    print("OUTPUT:", num1)
                    return num1
            new_i = i + 2
        elif opcode == JUMP_IF_TRUE:
            new_i = jump_if_true_f(num1, data_op, num2, i)
        elif opcode == JUMP_IF_FALSE:
            new_i = jump_if_false_f(num1, data_op, num2, i)
        elif opcode == LESS_THAN:
            less_than_f(num1, num2, data_op, data_op[i+3])
            new_i = i + 4
        elif opcode == EQUALS:
            equals_f(num1, num2, data_op, data_op[i+3])
            new_i = i + 4

        _, _, _, opcode_new = parse_opcode(data_op[i])
        if opcode == opcode_new:
            i = new_i

#         "if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

    return data_op


def jump_if_false_f(num1, data_op, num2, i):
    if num1 == 0:
        i = num2
    else:
        i += 3
    return i


def jump_if_true_f(num1, data_op, num2, i):
    if num1 != 0:
        i = num2
    else:
        i += 3
    return i


def less_than_f(num1, num2, data_op, num3_idx):
    if num1 < num2:
        data_op[num3_idx] = 1
    else:
        data_op[num3_idx] = 0


def equals_f(num1, num2, data_op, num3_idx):
    if num1 == num2:
        data_op[num3_idx] = 1
    else:
        data_op[num3_idx] = 0


with open(r"resources\day5.csv") as infile:
    data = infile.readline().split(",")
data = [int(x) for x in data]


# day5
assert opcode_runned(data, 1) == 4887191

assert opcode_runned(data, 5) == 3419022


#test

assert opcode_runned([3,9,8,9,10,9,4,9,99,-1,8], 8)  == 1 #ok
assert opcode_runned([3,9,7,9,10,9,4,9,99,-1,8], 7)  == 1 #ok

print(opcode_runned([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8))
