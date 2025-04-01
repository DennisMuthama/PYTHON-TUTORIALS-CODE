import random
import time


b = [0] * 50000


def merge(a, low, mid, high):
    i = low
    j = mid + 1
    k = low

    
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

  
    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1

   
    while j <= high:
        b[k] = a[j]
        j += 1
        k += 1

 
    for k in range(low, high + 1):
        a[k] = b[k]


def merge_sort(a, low, high):
    if low >= high:
        return

    mid = (low + high) // 2

  
    merge_sort(a, low, mid)
    merge_sort(a, mid + 1, high)

    
    merge(a, low, mid, high)


def main():
  
    n = int(input("Enter how many numbers: "))
    a = [0] * (n + 1)

    print("\nThe random numbers are:")
    for k in range(1, n + 1):
        a[k] = random.randint(0, 100000)
        print(a[k], end="\t")

    start_time = time.time()

    merge_sort(a, 1, n)

    end_time = time.time()
    total_time = end_time - start_time


    print("\n\nSorted numbers are:")
    for k in range(1, n + 1):
        print(a[k], end="\t")


    print(f"\n\nThe time taken is {total_time:.10f} seconds.")


if __name__ == "__main__":
    main()
