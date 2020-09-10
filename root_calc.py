def func():
    num = int(input('What is the number\n'))
    root = int(input('What is the power\n'))
    if root != 0 and root > 0:
        ans = num**(1/root)
        print(ans)
        return ans
    else:
        print("INVALID!!!!!!!🐙 ")
