def main():
    for number in range(10):
        c = cube(number)
        print(c)

def cube(value):
    cube_values = value * value * value # value ** 3 will also multiply value by 3 if set - can also do 4, 5, 6, etc
    return cube_values

main()