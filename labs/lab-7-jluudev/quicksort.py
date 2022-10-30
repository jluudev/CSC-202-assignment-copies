import random

PIVOT_FIRST = False
total_count = 0


def quick_sort(alist):
    global total_count
    total_count = 0
    quick_sort_helper(alist, 0, len(alist) - 1)
    return total_count


def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    global total_count
    piv_index = first
    if not PIVOT_FIRST:  # write code for selecting pivot based on median of 3 (first/mid/last)
        mid = (first + last) // 2
        a = alist[first]
        b = alist[mid]
        c = alist[last]
        if a <= b and b <= c:
            piv_index = mid
        elif c <= b <= a:
            piv_index = mid
        elif a <= c <= b:
            piv_index = last
        elif b <= c <= a:
            piv_index = last
        else:
            piv_index = first

    pivotvalue = alist[piv_index]
    alist[piv_index] = alist[first]  # move pivot out of the way
    alist[first] = pivotvalue  # by swapping with first element

    leftmark = first + 1  # left index
    rightmark = last  # right index

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            total_count += 1
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            total_count += 1
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    alist[first] = alist[rightmark]  # swap pivotvalue and element at rightmark
    alist[rightmark] = pivotvalue

    return rightmark  # return splitpoint


if __name__ == '__main__':
    n = 800

    my_randoms = random.sample(range(100000), n)
    count = quick_sort(my_randoms)
    print("n =", n, "Final:", my_randoms, "\n count =", count)

    my_list = list(range(n))
    quick_sort(my_list)
    print("n =", n, "Final:", my_list, "\n count =", total_count)

#first
# 10 runs n = 100: 651, 600, 567,  618, 638 581 600 596 680 647
# 10 runs n = 200: 1430, 1519 1651 1408 1679 1550 1647 1596 1540 1744
# 10 runs n = 400: 3284 3614 3304 3897 3684 3758 3773 3444 4114 3578
# 10 runs n = 800: 7930 8053 7508 9807 9252 7744 8927 7982 7686 9140

#median of 3s
#100: 547 519 548 565 584 537 531 533 540 522
#200: 1306 1355 1233 1460 1390 1278 1333 1298 1368 1236
#400: 3287 3185 3034 3203 3222 3456 3206 3053 3050 3113
#800: 7226 6863 7135 7144 6730 7444 7440 7425 6852 6883