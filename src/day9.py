

class Computer():
    def __init(self):
        self.relative_base = 0
        self.memory = []
    def get_input_values(self, param_value, memory, idx):
        POSITION_MODE = 0
        IMMEDIATE_MODE = 1
        RELATIVE_MODE = 2
        try:
            if param_value == POSITION_MODE:
                num = memory[memory[idx+1]]

            elif param_value == IMMEDIATE_MODE:
                num = memory[idx+1]
            elif param_value == RELATIVE_MODE:
                num = memory[self.relative_base + memory[idx+1]]

            return int(num)
        except:
            return None  # skipp num2-3-4 if not existing

    def parse_opcode(self, raw_opcode):
        full_opcode = str(raw_opcode).zfill(5)
        param_mode1 = int(full_opcode[-3])
        param_mode2 = int(full_opcode[-4])
        param_mode3 = int(full_opcode[-5])
        opcode = int(full_opcode[-2:])
        return param_mode1, param_mode2, param_mode3, opcode

    def opcode_runned(self, data_runner, o_input=None):
        self.memory = data_runner.copy() + [None]*10**6

        print("runner")

        ADD = 1
        MULTIPL = 2
        INPUT = 3
        OUTPUT = 4
        JUMP_IF_TRUE = 5
        JUMP_IF_FALSE = 6
        LESS_THAN = 7
        EQUALS = 8
        ADJUST_REL_BASE = 9

        i = 0
        iters = 0
        while iters < 5000:
            iters += 1
            if int(self.memory[i]) == 99:
                print("EXIT 99")
                break

            param_mode1, param_mode2, param_mode3, opcode = self.parse_opcode(
                self.memory[i])

            

            num1 = self.get_input_values(param_mode1, self.memory, i)
            num2 = self.get_input_values(param_mode2, self.memory, i+1)

            if opcode in [ADD, MULTIPL]:
                if opcode == 1:
                    def opfunc(x, y): return x+y
                elif opcode == 2:
                    def opfunc(x, y): return x*y
                    
                i_output = self.memory[i+3]
                self.memory[i_output] = opfunc(num1, num2)
                new_i = i + 4
            elif opcode in [INPUT, OUTPUT]:
                if opcode == INPUT:
                    self.memory[self.memory[i+1]] = int(o_input)
                    int(o_input)  # validation-light
                elif opcode == OUTPUT:

                    if num1 != 0:  # WTF?
                        print("OUTPUT:", num1)
                        return num1
                new_i = i + 2
            elif opcode == JUMP_IF_TRUE:
                new_i = jump_if_true_f(num1, self.memory, num2, i)
            elif opcode == JUMP_IF_FALSE:
                new_i = jump_if_false_f(num1, self.memory, num2, i)
            elif opcode == LESS_THAN:
                less_than_f(num1, num2, self.memory, self.memory[i+3])
                new_i = i + 4
            elif opcode == EQUALS:
                equals_f(num1, num2, self.memory, self.memory[i+3])
                new_i = i + 4
            elif opcode == ADJUST_REL_BASE:
                self.relative_base = num1
                new_i = i + 2

            _, _, _, opcode_new = self.parse_opcode(self.memory[i])
            if opcode == opcode_new:
                i = new_i

        return self.memory


def jump_if_false_f(num1, memory, num2, i):
    if num1 == 0:
        i = num2
    else:
        i += 3
    return i


def jump_if_true_f(num1, memory, num2, i):
    if num1 != 0:
        i = num2
    else:
        i += 3
    return i


def less_than_f(num1, num2, memory, num3_idx):
    if num1 < num2:
        memory[num3_idx] = 1
    else:
        memory[num3_idx] = 0


def equals_f(num1, num2, memory, num3_idx):
    if num1 == num2:
        memory[num3_idx] = 1
    else:
        memory[num3_idx] = 0


with open(r"resources\day9.csv") as infile:
    data = infile.readline().split(",")
data = [int(x) for x in data]


computer = Computer()
# day5


def day5():
    assert computer.opcode_runned(data, 1) == 4887191

    assert computer.opcode_runned(data, 5) == 3419022
    # test day5
    assert computer.opcode_runned(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8) == 1  # ok
    assert computer.opcode_runned(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7) == 1  # ok
    print(computer.opcode_runned([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                  1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                  999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8))


# day9
computer.opcode_runned([109, 1, 204, -1, 1001, 100, 1,
                        100, 1008, 100, 16, 101, 1006, 101, 0, 99])
assert len(str(computer.opcode_runned(
    [1102, 34915192, 34915192, 7, 4, 7, 99, 0]))) == 16
computer.opcode_runned([104, 1125899906842624, 99]) == 1125899906842624


# computer.opcode_runned(data,1)