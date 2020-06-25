import sys

print(sys.getsizeof(1))
print(sys.getsizeof(2**30-1))
print(sys.getsizeof(2**30))
print(sys.getsizeof(2**32))
print(sys.getsizeof(2**60)) # 每2**30增加4个字节
print(sys.getsizeof(2**90))