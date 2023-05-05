def solution(s):
    str_to_num = dict(zip(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
                         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))
    for i, j in str_to_num.items():
        s = s.replace(i,j)
        
    return int(s)