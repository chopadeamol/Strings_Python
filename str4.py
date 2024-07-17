"""
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s
first, middle, and last characters.
Given:
    s1 = "America"
    s2 = "Japan"
Expected Output:
    AJrpan
"""
def first_mid_last(s1,s2):
    s1_first = s1[0]
    s1_middle = s1[int(len(s1)/2)]
    s1_last = s1[-1]
    s2_first = s2[0]
    s2_middle = s2[int(len(s2)/2)]
    s2_last = s2[-1]
    s3 = s1_first + s2_first + s1_middle + s2_middle + s1_last + s2_last
    return s3

def main():
    s1 = "America"
    s2 = "Japan"
    sobj = first_mid_last(s1,s2)
    print(sobj)

if __name__ == "__main__":
    main()