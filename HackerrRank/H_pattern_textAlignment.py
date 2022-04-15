#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
''' rjust bcoz we need H to strt printing at the right side of the left side of the cone.
    Here (thickness-1) is the width, c*i gives the number of times H will be printed. If the width is 4, and the
    H are 2 times then the output will have 2 spaces and 2 H.
'''

#Top Pillars
for i in range(thickness+1):        # Thickness is describing the no of rows here, as its the end of the range.
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    '''Width 10'''                          '''Width 30'''

#Middle Belt
for i in range((thickness+1)//2):       #range is 3. // indicates that ans will be int.
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    '''The last rjust is added to whole pattern to shift it to right side. This was nested type.'''