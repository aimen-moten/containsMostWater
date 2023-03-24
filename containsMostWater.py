def maxArea(height: list[int]) -> int:
    maxA= 0
    currA= 0 
    minH = 0 
    i = 0
    j = len(height)-1
    while i < j:
        minH = min(height[i], height[j])
        currA = minH * (j-i)
        maxA = max(maxA, currA)
        if height[i] < height[j]:
            i +=1
        else:
            j -=1
    return maxA

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([1,8,6,2,5,4,7,3,8]))