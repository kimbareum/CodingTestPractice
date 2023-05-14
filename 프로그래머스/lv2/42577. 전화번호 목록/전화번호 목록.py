def solution(phone_book):
    phone_book_hash = dict.fromkeys(phone_book, 0)
    for phone in phone_book:
        for i in range(1,len(phone)):
            if phone[0:i] in phone_book_hash:
                return False
    return True