def solution(phone_book):
    # 전화번호부 정렬
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True