class Computer():
    def __init__(self):
        self.relative_base = 0
        self.memory = []
        self.output = []

    def get_input_index(self, param_value, idx):
        POSITION_MODE = 0
        IMMEDIATE_MODE = 1
        RELATIVE_MODE = 2
        memory = self.memory
        if param_value == POSITION_MODE:
            out_idx = memory[idx+1]

        elif param_value == IMMEDIATE_MODE:
            out_idx = idx+1
        elif param_value == RELATIVE_MODE:
            out_idx = self.relative_base + memory[idx+1]

        return int(out_idx)


    def get_input_values(self, param_value, idx):
        memory = self.memory
        try:
            out_idx = self.get_input_index(param_value, idx)
            num = memory[out_idx]
        except:
            print(f"Skipping {param_value}, idx {idx}")
            num = None  # skipp num2-3-4 if not existing
        return num

    def parse_opcode(self, raw_opcode):
        full_opcode = str(raw_opcode).zfill(5)
        param_mode1 = int(full_opcode[-3])
        param_mode2 = int(full_opcode[-4])
        param_mode3 = int(full_opcode[-5])
        opcode = int(full_opcode[-2:])
        return param_mode1, param_mode2, param_mode3, opcode

    def opcode_runned(self, data_runner, o_input=None):
        self.memory = data_runner.copy() + [0]*10**6

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
        while True:
            if int(self.memory[i]) == 99:
                print("EXIT 99")
                break

            param_mode1, param_mode2, param_mode3, opcode = self.parse_opcode(
                self.memory[i])

            num1 = self.get_input_values(param_mode1, i)
            num2 = self.get_input_values(param_mode2, i+1)
            num3 = self.get_input_values(param_mode3, i+2)
            i_num1 = self.get_input_index(param_mode1, i)
            i_num2 = self.get_input_index(param_mode1, i+1)
            i_num3 = self.get_input_index(param_mode3, i+2)

            if opcode in [ADD, MULTIPL]:
                if opcode == 1:
                    def opfunc(x, y): return x+y
                elif opcode == 2:
                    def opfunc(x, y): return x*y
                self.memory[i_num3] = opfunc(num1, num2)
                new_i = i + 4
            elif opcode in [INPUT, OUTPUT]:
                if opcode == INPUT:
                    self.memory[i_num1] = int(o_input)
                    int(o_input)  # validation-light
                elif opcode == OUTPUT:
                    self.output.append(num1)
                new_i = i + 2
            elif opcode == JUMP_IF_TRUE:
                new_i = jump_if_true_f(num1, self.memory, num2, i)
            elif opcode == JUMP_IF_FALSE:
                new_i = jump_if_false_f(num1, self.memory, num2, i)
            elif opcode == LESS_THAN:
                less_than_f(num1, num2, self.memory, i_num3)
                new_i = i + 4
            elif opcode == EQUALS:
                equals_f(num1, num2, self.memory, i_num3)
                new_i = i + 4
            elif opcode == ADJUST_REL_BASE:
                self.relative_base += num1
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


# day9
def test_day91():
    test1_input = [109, 1, 204, -1, 1001, 100, 1,
                   100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    computer.opcode_runned(test1_input)
    assert computer.output == test1_input


def test_day92():
    computer.opcode_runned(
        [1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    assert len(str(computer.output[0])) == 16


def test_day93():
    computer.opcode_runned([104, 1125899906842624, 99])
    assert computer.output[0] == 1125899906842624

# test_day93()



computer.opcode_runned(data, 2)
print(computer.output)
