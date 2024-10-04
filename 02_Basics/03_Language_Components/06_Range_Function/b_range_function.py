#!/usr/bin/python3

list(range(0))  # [] -> range(0, 0, 1)
list(range(1, 0))  # [] -> range(1, 0, 1)
list(range(1, 0, -1))  # [1]

r = range(0, 20, 2)
print(r)  

r.start  # 0
r.stop  # 20
r.step  # 2

print(
    f"""
  r.start: {r.start}
  r.stop:  {r.stop}
  r.step:  {r.step}
"""
)

11 in r  # False
10 in r  # True

r.count(11)  # 0
r.count(10)  # 1
r.index(10)  # 5

r[5]  # 10
r[:5]  # range(0, 10, 2)
r[-1]  # 18

range(0) == range(2, 1, 3)  # True
range(0, 3, 2) == range(0, 4, 2)  # True