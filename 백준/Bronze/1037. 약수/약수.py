n = int(input())
arr = [*map(int, input().split(' '))]
arr.sort()
print(arr[0] * arr[-1])