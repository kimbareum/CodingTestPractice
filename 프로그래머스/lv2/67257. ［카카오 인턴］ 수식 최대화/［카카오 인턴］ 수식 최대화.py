import re
def solution(expression):
    answer = 0
    _number = list(map(int,re.findall('[0-9]+', expression)))
    _operand = re.findall('[-*+]', expression)
    _opers = ['*','+','-']
    _cal = [(lambda x,y:x*y), (lambda x,y:x+y), (lambda x,y:x-y)]
    priority = [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]
    for p in priority:
        number = _number[:]
        operand = _operand[:]
        for i in p:
            temp_num = [number[0]]
            temp_oper = []
            for j in range(len(operand)):
                num = number[j+1]
                oper = operand[j]
                temp_num.append(num)
                temp_oper.append(oper)
                if temp_oper[-1] == _opers[i]:
                    num2, num1 = temp_num.pop(), temp_num.pop()
                    temp_oper.pop()
                    temp_num.append(_cal[i](num1, num2))
            number = temp_num
            operand = temp_oper
            if len(number) <= 1 and len(operand) <1:
                answer = max(abs(number[-1]),answer)
                break      
    return answer