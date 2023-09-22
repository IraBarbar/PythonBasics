from lesson_1.Lesson_6.task02.fun import find_num
from sys import argv


print(argv)
start, end, count_ = map(int, argv[1:])
print(start, end, count_)
find_num(start, end, count_)
