def power_mod(b, e, m):
    x = 1
    while e > 0:
        b, e, x = (b * b % m,
                    e // 2,
                    b * x % m 
                    if e % 2 
                    else x
                    )

    return x

a = int(input("Enter a number: "))
b = int(input("Enter the exponentiation: "))
m = int(input("Enter the mod: "))
print("The result is:" ,power_mod(a, b, m))