"""
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if
all the characters in the s1 are present in s2. The character’s position doesn’t matter.
Given:
    Case 1:                     Case 2:
    s1 = "Yn"                   s1 = "Ynf"
    s2 = "PYnative"             s2 = "PYnative"

Expected Output:                Expected Output:
    True                            False
"""
def check_presence(s1,s2):
    flag = True
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False
    return flag

def main():
    s1 = "Ynz"
    s2 = "PYnative"
    sobj = check_presence(s1,s2)
    print(sobj)

if __name__ == "__main__":
    main()