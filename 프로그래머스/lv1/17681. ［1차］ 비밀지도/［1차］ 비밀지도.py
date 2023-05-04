def solution(n, arr1, arr2):
    tresure_map = []
    for i,j in zip(arr1,arr2):
        temp = str(bin(i|j))[2:]
        tresure_map.append(temp.zfill(n).replace('0',' ').replace('1','#'))
    return tresure_map