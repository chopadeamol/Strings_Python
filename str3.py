"""
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
Given:
    s1 = "Ault"
    s2 = "Kelly"
Output:
    AuKellylt
"""
def append_string_in_middle(s1, s2):
    sl = len(s1)
    sm = int(sl / 2)
    a = s1[:sm]
    a = a + s2
    a = a + s1[sm:]
    return a

def main():
    s1 = "Ault"
    s2 = "Kelly"
    sobj = append_string_in_middle(s1, s2)
    print(sobj
          )
if __name__ == "__main__":
    main()
