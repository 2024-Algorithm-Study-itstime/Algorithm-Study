# 참고블로그 : https://velog.io/@ggb05224/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C%ED%98%84-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC-python
# 1. numbers 값을 이진수로 변환
# 2. 이진수 길이 : 노드 개수, 포화이진트리 노드 개수 : 2**n -1

# 먼저 포화이진트리로 만들기전 이진트리가 유효한지부터 검증해야한다. 가운데 노드가 0인데 왼쪽이나 오른쪽 자식 노드에 1이 있으면 유효하지 않다.

# 63 -> 111111 자릿수가 (2**n)-1 이 아니라면 앞에 0을 추가하여 0111111로 만든다. 
# 루트노드부터 시작해서 왼쪽 자식, 오른쪽 자식 검사 
# 0111111의 루트는 len(arr)//2로 idx =3이 루트. 

def dfs(b, i, depth):
    if depth == 0:  	# 리프 노드에 도달했다면
        return True 	# 포화이진트리
    
    # 부모노드가 '0' 일때
    # 왼쪽 자식 노드가 '1' 이거나 오른쪽 자식 노드가 '1' 이라면 포화 이진트리가 될 수 없음
    elif b[i] == '0':   
        if b[i - depth] == '1' or b[i + depth] == '1': return False

    # 왼쪽 서브 트리 탐색
    left = dfs(b, i - depth, depth // 2)
    # 오른쪽 서브 트리 탐색
    right = dfs(b, i + depth, depth // 2)
    return left and right
    
    
def solution(numbers):
    answer = []
    for num in numbers:				# num = 42
        b = bin(num)[2:]  			# b = 101010 / len(b) = 6
        nodes = bin(len(b) + 1)[2:] 	# nodes = 7 = 111
        
        # 포화이진트리가 아닌 경우 더미노드(0추가)
        if '1' in nodes[1:]:       
            dummies = (1 << len(nodes)) - int(nodes, 2)
            b = '0' * dummies + b
            
        # 이미 포화이진트리일 경우
        result = dfs(b, len(b)//2, (len(b)+1)//4)
        answer.append(1 if result else 0)
        
    return answer