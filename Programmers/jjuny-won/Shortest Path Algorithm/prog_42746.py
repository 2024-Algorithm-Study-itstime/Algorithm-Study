
def solution(numbers):
    
    numbers_str = list(map(str, numbers))
    
    # 두 문자열을 비교하여 정렬하는 커스텀 정렬 함수
    numbers_str.sort(key=lambda x: x*10, reverse=True)
    answer = ''.join(numbers_str)
    
    # '0'으로 시작한다면, 0을 반환 
    if answer[0] == '0':
        return '0'
    
    return answer

