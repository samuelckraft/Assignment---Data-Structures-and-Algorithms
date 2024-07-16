def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Task 1
    #The operation it performs is sorting the array by comparing the elements and swapping them if one is bigger than the other

#Task 2
    # O(n^2) meaning as the data sets increase, time will increase quadratically

#Task 3
def task3(arr):
    arr.sort()
    return arr

test = [64, 34, 25, 12, 22, 11, 90]

print(task3(test))