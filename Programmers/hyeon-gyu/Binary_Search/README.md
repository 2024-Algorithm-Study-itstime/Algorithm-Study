## 레벨 1
### 예산
이분탐색 공식 그대로 풀려고 하니 테스트 케이스 2개가 계속 실패했다.
한참 고민하고 나서 이분탐색이 아닌 그냥 총 예산에서 오름차순으로 정렬된 첫번째 인자부터 빼기 시작했고, 최대한 뺄 수 있는만큼 뺐을 때의 요소 갯수를 리턴해도
결국엔 예산이 0원이 되거나 남아도 같은 갯수였다.

### 삼총사
itertools 라이브러리를 통해서 조합을 이용했다.

from itertools import combinations
from itertools import permutations
는 항상 암기중이다.


## 레벨 2
### 타겟넘버
가능한 조합을 추출하는 방식으로 코드를 작성했다가 결국 못푼 문제
dfs로 +, -를 하나씩 더하는 모든 경우의 수를 만들고 값을 target값에 동일한 경우만 세는 문제.


### 전화번호 목록
처음엔 조합을 사용해서 문제를 해결하려고 했는데, 효율성 3번 4번을 해결하지 못했다.
아마 for문 돌면서 모든 조합을 만드는 데에서 시간이 오래 소요되는 것 같아서, 조합 없이 활용하는 방법에 대해서 고민을 해보았다.
문자열을 sort하면 시작문자가 유사한 문자열끼리 모이게 된다는 점에서 출발해서 문제를 해결했다.
startswith함수를 사용한게 핵심이라고 생각한다.

다른 사람들의 풀이를 보니 진정한 해시를 이용해서 푼 코드가 있어서 가져왔다.
```
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```

## 레벨 3
### 부대 복귀
처음 작성한 코드는 테스트11~15 시간초과 발생.
source 요소 하나씩 꺼내서 목적지까지 순회하지 않고, 거꾸로 목적지에서 부터 시작해 대기열이 빌때까지 인접한 노드들의 거리를 계산하여 기록해야한다.

### 파괴되지 않는 건물
3중 루프문으로 효율성 테스트를 통과하지 못했다. 
해설 참고 -> '누적합' 의 원리를 적용하여 시간복잡도를 O(1)로 낮춰야만 풀 수 있는 문제. 2차원 배열에서 누적합을 적용하여 최종적으로 board에 값을 더하여 최종값을 리턴해야한다.