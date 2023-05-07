import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+','.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        return 'aaa'
    if len(new_id) >= 16:
        new_id = new_id[0:15].rstrip('.')
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id