def solution(s):
    result = len(s)
    for i in range(1, len(s)//2+1):
        temp_zip = 0
        prev = s[0:i]
        count = 1
        string = ''
        for j in range(i,len(s),i):
            current = s[j:j+i]
            if prev==current:
                count += 1
            else:
                string += str(count)+prev if count != 1 else prev
                prev = current
                count = 1
        string += str(count)+s[j:] if count != 1 else s[j:]
        result = min(result, len(string))
    return result