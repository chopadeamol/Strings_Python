"""
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
Any leftover chars go at the end of the result.
Given:
    s1 = "Abc"
    s2 = "Xyz"
Output:
    AzbycX
"""
def mix_string(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    s3 = ""
    s2 = s2[::-1]
    length = s1_len if s1_len > s2_len else s2_len
    for i in range(length):
        if i < s1_len:
            s3 = s3 + s1[i]
        if i < s2_len:
            s3 = s3 + s2[i]
    return s3

def main():
    s1 = "Abc"
    s2 = "Xyz"
    sobj = mix_string(s1, s2)
    print(sobj)

if __name__ == "__main__":
    main()






