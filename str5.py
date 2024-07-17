"""
Given string contains a combination of the lower and upper case letters.
Write a program to arrange the characters of a string so that all lowercase letters should come first.
Given:
    str1 = "PyNaTive"
Expected Output:
    yaivePNT
"""
def upper_lower(str1):
    lower = []
    upper = []
    for i in str1:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    str2 = "".join(lower + upper)
    return str2

def main():
    str1 = "PyNaTive"
    sobj = upper_lower(str1)
    print(sobj)

if __name__ == "__main__":
    main()