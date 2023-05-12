def solution(arr1, arr2):
    arr2 = list(map(list, zip(*arr2)))
    answer =[]
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2)):
            suma = 0
            for k in range(len(arr1[0])):
                suma += arr1[i][k]*arr2[j][k]
            temp.append(suma)
        answer.append(temp)           
    return answer