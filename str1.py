"""
Write a program to create a new string made of an input string’s first, middle, and last character.
Given:
    str1 = "James"
    output = Jms
Hint:
    String index always starts with 0
    Use string indexing to get the character present at the given index
    Get the index of the middle character by dividing string length by 2
"""
def first_middle_last_char(string1):
    Ss = string1[0]
    Se = string1[-1]
    Sl = len(string1)
    Sm = int(Sl / 2)
    return Ss + string1[Sm] + Se

def main():
    string1 = "James"
    sObj = first_middle_last_char(string1)
    print(sObj)
if __name__ == "__main__":
    main()

