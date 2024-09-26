d=int(input("請輸入一個十進制數字:"))
decimal_number=d
b=bin(d)
c=oct(d)
e=hex(d)
print(b)
print(c)
print(e)
print('{:08b}'.format(d,'b')) #b=二進位
print('{:03o}'.format(d,'o')) #o=八進位
print('{:03x}'.format(d,'x'))