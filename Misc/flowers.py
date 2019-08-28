import bisect
import sys


def kEmptySlots( flowers, k):
    """
    :type flowers: List[int]
    :type k: int
    :rtype: int
    """
    garden = [[i - 1, i + 1] for i in range(len(flowers))]
    print(garden)
    garden[0][0], garden[-1][1] = None, None
    print(garden)
    ans = -1
    for i in range(len(flowers) - 1, -1, -1):
        cur = flowers[i] - 1
        print(cur)
        left, right = garden[cur]
        print("LR:_",left,right)
        if right != None and right - cur == k + 1:
            ans = i + 1
        if left != None and cur - left == k + 1:
            ans = i + 1
        if right != None:
            garden[right][0] = left
        if left != None:
            garden[left][1] = right
    return ans


flowers = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4]
k = 2

print("final result is :-",kEmptySlots(flowers,k))






