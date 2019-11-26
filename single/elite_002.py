#列表推导式，通过if过滤元素
a = [x*2 for x in range(100) if x %9==0]
print(a)
#列表推导式
cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)

#字典推导式，计算字符次数
my_text = " i love your ,i love sex, i love python"
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)