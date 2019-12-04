single_pw_list = [0,0,0,0,0,0]

"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
"""
# 138241-674034.
start = 138241   
stop = 674034
valid = []
# pw_range = [x for x in range(start,stop+1)]
for item in range(start,stop+1):
    got_double = False
    decreasing = False
    single_pw_list = [int(x) for x in str(item)]
    for i, number in enumerate(single_pw_list):
        try:
            if single_pw_list[i] == single_pw_list[i+1]:
                got_double = True
        except IndexError:
            pass
        try:
            if single_pw_list[i+1] < single_pw_list[i]:
                decreasing = True
        except:
            pass

    if got_double and not decreasing:
        valid.append(item)
print("sum",valid, len(valid))



