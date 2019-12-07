def opcode_runned(data_runner):
    data_op = data_runner.copy()
    for i in range(0,len(data_op),4):
        opcode = data_op[i]
        if opcode == 1:
            opfunc = lambda x,y: x+y
        elif opcode == 2:
            opfunc = lambda x,y: x*y
        elif opcode == 99:
            break

        i_num1 = data_op[i+1]
        i_num2 = data_op[i+2]
        i_output = data_op[i+3]
        data_op[i_output] = opfunc(data_op[i_num1],data_op[i_num2])
    return data_op


with open(r"resources\day2.csv") as infile:
    data = infile.readline().split(",")
data = [int(x) for x in data]

assert opcode_runned([1,0,0,0,99]) == [2,0,0,0,99]
assert opcode_runned([2,3,0,3,99]) == [2,3,0,6,99]
assert opcode_runned([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert opcode_runned([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

def prerunner(data,n=12, v = 2):
    data[1]=n
    data[2]=v
    return opcode_runned(data)[0]
# part 1
assert prerunner(data) == 9581917
print("1 done", data[0])

#part2
def part2(data):   
    for n in range(100):
        for v in range(100):
            if prerunner(data,n,v) == 19690720:
                print(f"2. {100 * n + v}")
                break
part2(data)
