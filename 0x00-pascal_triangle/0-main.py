#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Test case with n = 5
    print("Pascal's Triangle with n = 5:")
    print_triangle(pascal_triangle(5))
    print("\n")

    # Test case with n = 1
    print("Pascal's Triangle with n = 1:")
    print_triangle(pascal_triangle(1))
    print("\n")

    # Test case with n = 0
    print("Pascal's Triangle with n = 0 (should be empty):")
    print_triangle(pascal_triangle(0))
    print("\n")

    # Test case with n = 10
    print("Pascal's Triangle with n = 10:")
    print_triangle(pascal_triangle(10))
    print("\n")

    # Test case with n = 100
    # Uncomment the following line to test for n = 100 (very large output)
    # print_triangle(pascal_triangle(100))

