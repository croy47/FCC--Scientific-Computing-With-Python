def arithmetic_arranger(problems, calc=False):  
#  
    operands_list = []
    operators_list = []
    calculated_list = [] 

    if len(problems) > 5:
        return "Error: Too many problems."
# 
    for problem in problems:
        problem_input = problem.split()
        operands_list.extend([problem_input[0], problem_input[2]])
        operators_list.extend([problem_input[1]])  
# 
    for operand in operands_list:
        if len(operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not operand.isnumeric():
            return 'Error: Numbers must only contain digits.'
# 
    for operator in operators_list:
        if not (operator == '+' or operator == "-"):
            return "Error: Operator must be '+' or '-'."

# ALL ERRORS TAKEN CARE OF. TIME TO EVALUATE AND ARRANGE.
    for problem in problems:
        if calc == True:
            calculated_list.extend([eval(problem)])

    first_line = ''
    second_line = ''
    dashed_line = ''
    calculated_line = ""

    for i in range(len(operands_list)):
        if i % 2 == 0:
            # 2 has been added as actual length has one operator and a space extra
            bigger_len = len(operands_list[i]) + 2 if len(operands_list[i]) > len(operands_list[i + 1]) else len(operands_list[i + 1]) + 2 
            diff = len(operands_list[i]) - len(operands_list[i + 1])
            # TypeError: Str + int & index out of range  
            calculated_line += (bigger_len - len(str(calculated_list[i//2]))) * " " + str(calculated_list[i//2]) + " " * 4 if calc else ""
            # print(i)
           
            if diff < 0:
                first_line += " " * (abs(diff) + 2) + operands_list[i] + " " * 4
                second_line += operators_list[i // 2 ] + " " + operands_list[i + 1] + " " * 4
                dashed_line += bigger_len * '-' + " " * 4 
                
            else:
                first_line += " " * 2 +  operands_list[i] + " " * 4
                second_line += operators_list[i // 2] +  " " * (abs(diff) + 1) + operands_list[i + 1] + " " * 4
                dashed_line += bigger_len * '-' + " " * 4
                
    
    # print(first_line)
    # print(second_line)
    # print(dashed_line)
    # print(calculated_line)
    if calc:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashed_line.strip() + '\n' + calculated_line.rstrip() 
    else:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashed_line.strip()
    return arranged_problems



# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))
# print(arithmetic_arranger(["1 + 2", "1 - 9380"], True))
# print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], True))
# print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))



