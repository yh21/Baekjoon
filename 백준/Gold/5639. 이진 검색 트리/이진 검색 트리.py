import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.read
nums = list(map(int, input().split()))

def postorder(start, end):
    if start > end:
        return

    root = nums[start]
    idx = end + 1
    for i in range(start + 1, end + 1):
        if nums[i] > root:
            idx = i
            break
    
    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)

postorder(0, len(nums) - 1)