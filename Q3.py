def is_even_or_odd(a):
    return (a % 2 == 0 and "偶數") or "奇數"
a = int(input("請輸入一個整數: "))
print(f"{a} 是 {is_even_or_odd(a)}")