def minMaxSum(arr):
    sum_list = []
    duplicate = []
    for i in arr:
        duplicate.append(i)

    def sum(arr):
        s = 0
        for i in arr:
            s += i
        return s

    for i in range(len(arr)):
        arr[i] = 0
        sum_list.append(sum(arr))
        arr[i] = duplicate[i]

    max_value = max(sum_list)
    min_value = min(sum_list)
    print(min_value,max_value)
minMaxSum([1,2,3,4,5])
