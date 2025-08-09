num = list(map(int, input().split()))
a = max(num)
b = min(num)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(a * b // gcd(a, b))