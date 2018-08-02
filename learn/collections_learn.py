# namedtuple
from collections import namedtuple, deque, defaultdict, OrderedDict

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
# namedtuple('名称', [属性list]): 用namedtuple表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
d = deque(['a', 'b', 'c'])
# 在尾部增加
d.append('x')
# 在头部增加
d.appendleft('y')
print(d)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict

dd = defaultdict(lambda : 'null')
dd['x'] = 1
print(dd['x'])
print(dd['y'])

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict (可排序的字典)

