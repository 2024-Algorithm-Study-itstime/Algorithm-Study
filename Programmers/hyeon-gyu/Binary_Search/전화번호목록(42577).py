from itertools import combinations

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in combinations(phone_book,2):
        a1 = i[0]
        a2 = i[1]
        if a2.startswith(a1):
            answer = False
            break
        if a1.startswith(a2):
            answer = False
            break
    return answer



def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    return answer