

## 베스트 앨범 (해결)

### 접근방식
1. 장르별 토탈 재생수 구해서 장르 우선순위 구하기
2. 장르별로 재생수 우선순위 매기기
3. 장르별로 상위 두개씩만 

```
장르와 재생리스트가 만개 이하라서 2중 for loop는 절대 안되고
무조건 딕셔너리로 완성해야한다고 생각함.

딕셔너리를 활용해서 장르별 토탈 재생수 자료구조 만들고
총 재생수를 기준으로 내림차순 결과값 보여주는 딕셔너리 생성

추가로 장르별 (재생횟수, 고유번호) 를 리스트로 가지는 딕셔너리 하나 더 생성하여 람다 함수로 재생횟수 기준 내림차순 정렬 진행

루프 돌면서 2개씩만 answer에 담아서 리턴
```

### sort(), sorted() 함수 활용 방법

파이썬 내장함수 sort()는 시간복잡도 로 주로 활용한다.
리스트를 뒤집거나 특정 요소를 기준으로 정렬을 하는 방법은 외우는게 좋아보인다.

sort(key=len) : 길이를 기준으로 정렬

res = sorted(arr, reverse=True) : 배열을 내림차순으로 정렬 (기본값은 오름차순)

people = [("John", 30), ("Daisy", 25), ("Anne", 35)]

people.sort(key=lambda x: x[1]) :  나이에 따라 사람 정렬
people.sort(key=lambda x: (x[1], x[0])) : 나이가 동일하다면 이름순으로 정렬


-----------

### 불량 사용자 (미해결)
- 처음 접근 방식
1. banned_id와 user_id로 2중 for loop 시작  ( '입력 리스트들의 항목 갯수가 100개 이하다'. 라는 제한이 없어서 시간초과가 걱정되긴 했지만 진행함)
2. user_id와 banned_id 길이가 동일한지 먼저 확인
3. 루프 돌다가 banned_id의 요소가 *이라면 continue, 단어 하나씩 비교하다가 하나라도 다르면 리턴

- 틀린 접근
``` user_id를 가지고 banned_id 요소 갯수 만큼 조합을 활용해서 비교군을 만들었다. 도저히 안풀려서 다른 풀이들을 검색하게 되었고 조합이 아니라 순열로 비교군을 만들어야했었다. 테스트 케이스 중 ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"] 가 입력값으로 들어온다면 [frodo, crodo, abc123] , [frodo, crodo, frodoc] 결국 이 두가지 밖에 될 수가 없다. 순열이 아닌 조합을 사용해버리면  frodo와 crodo가 어떤 순서로 *rodo와 매치되는지에 따른 경우의 수를 놓치게 된다. ```