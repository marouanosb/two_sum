def two_sum(num_list, target):
    num_dict = {}
    for i, num in enumerate(num_list):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i 
        
    return []

def two_sum_2(num_list, target):    #when list is ordered
    i = 0
    j = len(num_list) - 1
    while i != j:
        if num_list[i] + num_list[j] > target:
            j = j-1
        elif num_list[i] + num_list[j] < target:
            i = i+1
        else:
            return [i,j]

    return []


    


if __name__ == "__main__" :
    nums = [2,1,15,7,10,5]
    nums_ordered = [1,2,5,7,10,15]
    result = two_sum(nums, 15)
    if result == []:
        print("No possible matches.")
    else: 
        print(nums[result[0]], nums[result[1]])

    result2 = two_sum_2(nums_ordered, 15)
    if result2 == []:
        print("No possible matches.")
    else: 
        print(nums_ordered[result2[0]], nums_ordered[result2[1]])