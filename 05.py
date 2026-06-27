import copy

def deep_reverse(x):
    if isinstance(x,list):
        ret=[]
        for i in reversed(x):
            ret.append(deep_reverse(i))
    elif isinstance(x,tuple):
        ret=tuple(deep_reverse(i) for i in reversed(x))
    else:
        ret=x
    return ret
T = int(input())
for _ in range(T):
    obj = eval(input())
    backup = copy.deepcopy(obj)
    result = deep_reverse(obj)
    assert obj == backup, "输入对象被修改"
    print(result)
