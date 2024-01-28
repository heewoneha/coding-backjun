n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

left = 0
right = n-1
answer = 0

while left < right:
    tmp = nums[left] + nums[right]
    if tmp > x:
        right -= 1
    elif tmp < x:
        left += 1
    else:
        answer += 1
        right -= 1

print(answer)
