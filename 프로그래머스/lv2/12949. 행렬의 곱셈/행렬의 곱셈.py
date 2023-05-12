def solution(arr1, arr2):
    arr2 = list(map(list, zip(*arr2)))
    answer =[]
    for i in arr1:
        temp = []
        for j in arr2:
            suma = 0
            for k in range(len(arr1[0])):
                suma += i[k]*j[k]
            temp.append(suma)
        answer.append(temp)           
    return answer