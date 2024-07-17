"""
Count all letters, digits, and special symbols from a given string
Given:
    str1 = "P@#yn26at^&i5ve"
Output:
    Total counts of chars, digits, and symbols
    Chars = 8
    Digits = 3
    Symbol = 4
"""
def counts(str1):
    """First Way to count """
    digits = []
    chars = []
    symbols = []
    for i in str1:
        if i.isdigit():
            digits.append(i)
        elif i.isalpha():
            chars.append(i)
        else:
            symbols.append(i)
    print("Digits:",len(digits), "Chars:",len(chars), "Symbol:",len(symbols))

    """Second Way to count"""
    digit = 0
    char = 0
    symbol = 0
    for j in str1:
        if j.isdigit():
            digit += 1
        elif j.isalpha():
            char += 1
        else:
            symbol += 1
    print("digit: ", digit, "char:",char, "symbol:",symbol)


def main():
    str1 = "P@#yn26at^&i5ve"
    sobj = counts(str1)
    # print(sobj)

if __name__ == "__main__":
    main()