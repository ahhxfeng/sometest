#! env/bin/ pytthon
# coding= utf-8

def Soulution(a, b):
    if a is None or b is None:
        print("should not be null")
        return 0

    tmp = gcd(a, b)

    result = a * b / tmp
    return result

def gcd(a, b):
    if a is None or b is None:
        print("should not be null")
        return 0
    # 交换大小
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    prompt = '''
    This program is to find the common multipule of two numbers
    Please input(Spearted by space):
    '''
    print(prompt)
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    result = Soulution(a, b)
    print("result:", result)