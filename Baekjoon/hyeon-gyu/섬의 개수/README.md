
- 탐색 문제라고 생각했고, 어떤 걸로 풀어도 괜찮을거라고 생각했습니다. 섬의 개수를 세야하기 때문에 결국 지도 전체를 탐색해야한다고 판단을 했습니다.
- 구현은 DFS 방식으로 재귀함수를 통해서 문제를 해결했습니다. 탐색범위가 상하좌우 뿐만 아니라 대각선 방향까지 움직이는 범위를 넓혀주었고, 방문한 곳은 '바다'로 처리했습니다
- 테스트결과는 모두 참으로 나왔는데 코드를 제출해보니 런타임에러가 발생했고, 검색해보니 백준 온라인 저지에선 '재귀 호출 깊이 제한'을 설정하지 않으면 런타임에러가 발생한다고 함. - https://www.acmicpc.net/board/view/138246
` 더해서 input 속도를 높이기 위해 input = sys.stdin.readline` 를 활용했습니다.

- 아마 지도의 크기가 매우 컸다면 2중 loop로 지도 전체를 탐색하는 과정에서 에러가 발생할 가능성이 있지만, w,h가 50 이하라서 전체를 탐색하도록 코드를 작성했습니다.