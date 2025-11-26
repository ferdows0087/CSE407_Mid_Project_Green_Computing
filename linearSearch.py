import random
import time


# Linear Search Function

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



# Generate a Large Dataset

def generate_large_dataset(size):
    # Generate unique numbers and sort them
    data = random.sample(range(1, size * 10), size)
    return data  # Linear search works on unsorted array too



# Run Linear Search Multiple Times

def run_linear_search():
    print("Generating large dataset...")
    arr = generate_large_dataset(1000000)  # 1 million numbers
    print("Dataset created!\n")

    target = arr[len(arr)//2]  # Choose middle value

    print("Running Linear Search 50 times...")
    start_time = time.time()

    for i in range(50):  # Run multiple times to make it noticeable
        linear_search(arr, target)

    end_time = time.time()
    print(f"Linear Search completed!")
    print(f"Total time taken: {end_time - start_time:.4f} seconds")



# Main Program

if __name__ == "__main__":
    run_linear_search()
