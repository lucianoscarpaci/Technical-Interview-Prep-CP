# Given an integer array engagements sorted in non-decreasing order,
# return an array of the squares of each number sorted
# in non-decreasing order.
# Task: Modify the solution to use the two-pointer technique.
def engagement_boost(engagements):
    squared_engagements = [] #[-4, -1, 0, 3, 10]
    
    for i in range(len(engagements)): # 0, 1, 2, 3, 4
        squared_engagement = engagements[i] * engagements[i] # 16, 1, 0, 9, 100
        squared_engagements.append((squared_engagement, i)) #[16,0], [1,1], [0,2], [9, 3], [100,4]
    
    squared_engagements.sort(reverse=True)#[100,4], [16,0], [9,3], [1,1], [0,2]
    
    left = 0 #represents l
    right = len(engagements) - 1 #4 #represents r
    position = right
    #for square, original_index in squared_engagements:
    #    result[position] = square #[0,0,0,0,100], [0,0,0,16,100], [0,0,9,16,100], [0,1,9,16,100], [0,1,9,16,100]
    #    position -= 1 #3, 2, 1, 0, -1
    result = [0] * len(engagements) #[0,0,0,0,0]
    while left <= right:
        left_square = engagements[left] * engagements[left] #16
        right_square = engagements[right] * engagements[right]
        
        if left_square > right_square: # error 16, replaced 100
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1
    
    return result #[0,1,9,16,100]

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
