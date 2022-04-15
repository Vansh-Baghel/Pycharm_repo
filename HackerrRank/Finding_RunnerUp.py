if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))  # N integers separated by space in an array by split.
                                          # List of values are accepted by the list word. For loop lagata toh
                                          # the condition jo same and line with space thi vo satisfy nhi hoti.

    a = max(arr)                          # Inbuilt function to find the maximum.
    for i in range(n):
        if a==max(arr):                 #This will trace all the max values.
            arr.remove(max(arr))        #This will remove all the max values.
    print(max(arr))                     #The 2nd max will be the current maximum.