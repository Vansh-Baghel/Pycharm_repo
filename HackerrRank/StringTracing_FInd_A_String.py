def count_substring(string, sub_string):
    c = 0
    l = len(sub_string)

    for i in range(len(string)):
        a = string[i:i + l]         # i will keep iterating, l is the length of sub string.
        if a == sub_string:         # a will be [0:3] means will check from (0 to 2) k char from string then
                                    # [1,4] then [2,5] from the string.
            c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)