txt = sorted(tuple(x for x in input().lstrip()))
txt_set = set()

for i in txt:
    if i not in txt_set:
        print(f"{i}: {txt.count(i)} time/s")
        txt_set.add(i)
