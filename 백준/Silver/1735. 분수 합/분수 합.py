div1 = list(map(int, input().split()))
div2 = list(map(int, input().split()))
n1 = div1[0]
n2 = div1[1]
n3 = div2[0]
n4 = div2[1]

denominator = n2 * n4
numerator = n1 * n4 + n2 * n3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd = gcd(denominator, numerator)

print(numerator // gcd, denominator // gcd)