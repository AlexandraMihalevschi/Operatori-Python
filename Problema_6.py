n = 9761
print("A:", n%10)
print("B:", n%100//10)
print("C:", n%9)
print("  ", n//9)
d = 0
s = 0
while(n > 0):
    d = int(n%10)
    s = s+d
    n = n/10
print("D:", s)
#Partea asta nu-mi reusea. imi dadea eroare
print("E: ?")