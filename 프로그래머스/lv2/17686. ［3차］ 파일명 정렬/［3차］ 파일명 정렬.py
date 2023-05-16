import re
def solution(files):
    p = re.compile(r'([^0-9]+)([0-9]+)(.+)?')
    split = []
    for i in files:
        split.extend(p.findall(i))
    split.sort(key = lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in split]