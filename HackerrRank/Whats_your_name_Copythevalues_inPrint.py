# Two methods to print values into print stmts.
def print_full_name(first, last):
    print("Hello " + first + " " + last + "!" + " You just delved into python.", )
    print("Hello {0} {1}! You just delved into python.".format(first, last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)