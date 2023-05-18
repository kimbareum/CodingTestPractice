def length_of_lis(nums):
    answer = [0]
    data = [(0, nums[0])]
    for num in nums[1:]:
        if data[-1][1] < num:
            answer.append(data[-1][0] + 1)
            data.append((data[-1][0] + 1, num))
        else:
            left = 0
            right = len(data) - 1
            while left < right:
                mid = (left + right) // 2
                if data[mid][1] < num:
                    left = mid + 1
                else:
                    right = mid
            data[right] = (right, num)
    return max(answer) + 1
