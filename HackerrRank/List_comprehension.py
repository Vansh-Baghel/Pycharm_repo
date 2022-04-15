x = int(input())
y = int(input())
z = int(input())
n = int(input())

''' res=[]
 for i in range (x+1):
      for j in range (y+1):
          for k in range (z+1):
              if i+j+k !=n:
                res.append ([i,j,k])
[expression for. condt] '''

res=[[i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if i+j+k !=n]
# This method is list comprehension where we completed the code in a single line.
print(res)