
d1={"amit":21,"rupali":2005, 15:"ajay",6.7:81.78}
print(d1);

print(d1.keys());

print(d1.values());

for i in d1:
    print(i,d1[i]);


d2=dict(one=1, two=2, three=3, four=4);
print(d2);
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# d3=dict(1="one", 2="two"); // can not give key as number it should be only string without single quates when we use dict() method
# print(d2); 
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

print(d2.get("one")); 
# 1

print(d2.keys())
# dict_keys(['one', 'two', 'three', 'four'])

print(d2.items())
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

print(d2.pop("three"))
# 3

print(d2);
# {'one': 1, 'two': 2, 'four': 4}

print(d2.popitem());
# ('four', 4)

d2.update({"two":"Raju Singh"})
print(d2);
# {'one': 1, 'two': 'Raju Singh'}

d2.setdefault(3,"ajinkya")
print(d2);
# {'one': 1, 'two': 'Raju Singh', 3: 'ajinkya'}

d3 = d2.copy();
print(d3);
# shallow copy
# {'one': 1, 'two': 'Raju Singh', 3: 'ajinkya'}

d4={1:"one", 2:"two", 3:[11,12]}
d5=d4.copy();
print(d5);
#! Shallow copy
# {1: 'one', 2: 'two', 3: [11, 12]}

d5[3].append(13);
print(d4)
# {1: 'one', 2: 'two', 3: [11, 12, 13]}
print(d5);
# {1: 'one', 2: 'two', 3: [11, 12, 13]}

import copy
d6=copy.deepcopy(d4);
print(d6);
#! ḍeep copy
# {1: 'one', 2: 'two', 3: [11, 12, 13]}

d6[3].append(14)
print(d4);
# {1: 'one', 2: 'two', 3: [11, 12, 13]}
print(d6);
# {1: 'one', 2: 'two', 3: [11, 12, 13, 14]}
