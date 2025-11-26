import random
import time

# Binary Search Function

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



# Generate a Large Dataset

def generate_large_dataset(size):
    # Generate unique numbers and sort them
    data = random.sample(range(1, size * 10), size)
    data.sort()
    return data



# Run Binary Search Multiple Times

def run_binary_search():
    print("Generating large dataset...")
    arr = generate_large_dataset(1000000)  # 1 million numbers
    print("Dataset created!\n")

    target = arr[len(arr)//2]  # Choose middle value

    print("Running Binary Search 50 times...")
    start_time = time.time()

    for i in range(50):  # Run multiple times to make it noticeable
        binary_search(arr, target)

    end_time = time.time()
    print(f"Binary Search completed!")
    print(f"Total time taken: {end_time - start_time:.4f} seconds")



# Main Program

if __name__ == "__main__":
    run_binary_search()
