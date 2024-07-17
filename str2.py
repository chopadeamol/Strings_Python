"""
Write a program to create a new string made of the middle three characters of an input string.
Case 1
    str1 = "JhonDipPeta"
    Output: Dip
Case 2
    str2 = "JaSonAy"
    Output: Son
Hint:
    First, get the middle index number by dividing string length by 2.
Use string slicing to get the middle three characters starting from the middle index to the next two character.
"""
def middle_three(str1):
    sl = len(str1)
    sm = int(sl / 2)
    st = str1[sm - 1:sm + 2]
    return st

def main():
    str1 = "JhonDipPeta"
    sobj1 = middle_three(str1)
    print(sobj1)

    str2 = "JaSonAy"
    sobj2 = middle_three(str2)
    print(sobj2)

if __name__ == "__main__":
    main()

