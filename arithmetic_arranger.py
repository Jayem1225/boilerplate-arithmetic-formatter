def _error_handling(s_num1, s_num2, op):
    if op not in [PLUS, MINUS]:
        return "Error: Operator must be '+' or '-'."
    try:
        num1 = int(s_num1)
        num2 = int(s_num2)
    except ValueError:
        return "Error: Numbers must only contain digits."
    if len(s_num1) > 4 or len(s_num2) > 4:
        return "Error: Numbers cannot be more than four digits."
    return None

def arithmetic_arranger(problems):
    probs = problems[0]
    answers = len(problems) > 1 and problems[1]
    PLUS = '+'
    MINUS = '-'
    
    if len(probs) > 5:
        return "Error: Too many problems."
        
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    
    for prob in probs:
        parts = prob.split()
        s_num1 = parts[0]
        s_num2 = parts[2]
        op = parts[1]
        
        error = _error_handling(s_num1, s_num2, op)
        if error:
            return error
        
        num1 = int(s_num1)
        num2 = int(s_num2)
        max_num_len = max([len(str(num1)), len(str(num2))])
        prob_width = max_num_len + 2
        row1.append(s_num1.rjust(prob_width))
        row2.append(op + s_num2.rjust(prob_width - 1))
        row3.append("-"*(prob-width))
        if answers:
            if op == PLUS:
                row4.append(str(num1+num2).rjust(prob_width))
            else:
                row4.append(str(num1-num2).rjust(prob_width))

    arranged_problems = f"""{'    '.join(row1)}
    {'    '.join(row2)}
    {'    '.join(row3)}"""
    
    if answers:
        arranged_problems += "\n" + "    ".join(row4)
    
    return arranged_problems
