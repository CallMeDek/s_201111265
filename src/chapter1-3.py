
word = ['sangmyung university', 'university']

d = dict()
for c in word:
    for e in c.split():
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

print "키-키값", d
print "저장된 문자의 갯수 ", len(d)
print "키: ", d.keys()

word = ['sangmyung university', 'university']

d = dict()
for c in word:
    for e in c.split():
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

print "키-키값", d
print "저장된 문자의 갯수 ", len(d)
print "키: ", d.keys()
print "키값: ", d.values()
