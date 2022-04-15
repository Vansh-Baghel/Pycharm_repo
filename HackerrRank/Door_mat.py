n, m = map(int, input().split())
s1 = '.|.'
s2 = 'WELCOME'
# part 1. upper
for i in range(n // 2):
    print((s1 * ((i * 2) + 1)).center(m, '-'))  # Brackets dhyaan se daalna warna error show hoga.

# part 2. middle
print(s2.center(m,"-"))

# part 3. Lower
for i in range((n // 2)-1,-1,-1):        # range (start value, end value, decrement). range ka end value is -1 bcoz
                                         # we wanted 0 as the end value. EG:- range(2):- 0,1
    print((s1 * ((i * 2)+1)).center(m, '-'))

