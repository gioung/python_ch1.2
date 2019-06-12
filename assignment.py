# 치환문의 예

a = 1
b = a + 1

print(a, b, sep=':')

# 세미콜론으로 치환문을 구분할 수 있다. (한줄 쓸 때)
e = 3.5; f = 5.3
print(e, f)

# 여러개를 한번에 치환하기 (위에거랑 같다. packing , unpacking)
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 대입
x = y = z = 10
print(x, y, z)
# 정수값은 primitive type 이 아니라 object type 이다. 내부적으로 pool을 쓴다.
a = 1  # integer type
print(a, type(a), id(a))
c = 1
a = 2
print(c, type(c), id(c))
print(a, type(a), id(a))
print(id(10))
# 확장 치환문
a = 10
a += 10
print(a)