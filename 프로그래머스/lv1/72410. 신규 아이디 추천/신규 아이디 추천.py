import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+','.', new_id)
    
    # st = re.sub('^[.]|[.]$', '', st)
    new_id = new_id.strip('.')
    
    # st = 'a' if len(st) == 0 else st[:15]
    if new_id == '':
        return 'aaa'
    if len(new_id) >= 16:
        new_id = new_id[0:15].rstrip('.')
    
    #st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id