def search(nums, num):
    for i in range(len(nums)):
        if nums[i]==num:
            return i
        



def binary_search(nums, num):
    low = 0
    high = len(nums)-1
    cnt=0
    while low <= high:
        mid = (low+high)//2
        guess = nums[mid]

        if guess<num:
            low=mid+1
        elif guess>num:
            high=mid-1

        else:
            return mid, cnt
        

nums=[1,3,4,6,7,8,9]
print(search(nums, 8))
print(binary_search(nums, 3))








