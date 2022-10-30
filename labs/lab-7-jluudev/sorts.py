import random
import time


def selection_sort(alist):
    num_comp = 0
    for i in range(len(alist)):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j

            num_comp += 1
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return num_comp


def insertion_sort(alist):
    num_comp = 0
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0:
            if value < alist[j]:
                check = True
            else:
                check = False

            num_comp += 1

            if check:
                alist[j + 1] = alist[j]
                alist[j] = value
                j = j - 1
            else:
                break
    return num_comp


def main():
    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = selection_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)


if __name__ == '__main__':
    main()
