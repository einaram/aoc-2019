def opcode_runner(data):
    data = [int(x) for x in data]
    for i in range(0,len(data),4):
        opcode = data[i]
        if opcode == 1:
            opfunc = lambda x,y: x+y
        elif opcode == 2:
            opfunc = lambda x,y: x*y
        elif opcode == 99:
            break

        i_num1 = data[i+1]
        i_num2 = data[i+2]
        i_output = data[i+3]
        data[i_output] = opfunc(data[i_num1],data[i_num2])
    return data


with open(r"resources\day2.csv") as infile:
    data = infile.readline().split(",")

assert opcode_runner([1,0,0,0,99]) == [2,0,0,0,99]
assert opcode_runner([2,3,0,3,99]) == [2,3,0,6,99]
assert opcode_runner([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert opcode_runner([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]


data[1]=12
data[2]=2
data =opcode_runner(data)
print(data)
print(data[0])