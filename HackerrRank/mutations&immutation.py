# Tuples (), string {}:- Unmutable
# List[]:- Mutable

def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    """Here join fn replaced "a" with "k"
    Insert use krta toh it wouldve inserted & not replaced. And cant use replace
    bcoz replace is not for list.
    """
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)