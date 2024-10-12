def binarySearch(arr, target):
    # Initialize the lower and upper bound
    low, high = 0, len(arr) - 1
    while low <= high:
        # Check the middle element
        mid = (low + high) // 2
        guess = arr[mid]
        # Found the target
        if guess == target:
            return mid
        # The guess was too high
        elif guess > target:
            high = mid - 1
        # The guess was too low
        else:
            low = mid + 1
        # The target doesn't exist in the array
    return None

input = [1, 3, 5, 7, 10, 11]
target = 3

# Test case 1
print(binarySearch(input, target)) # 1

# Test case 2
input = ["Apple", "Banana", "Cherries", "Grapes", "Orange"]
target = "Grapes"
print(binarySearch(input, target)) # 3