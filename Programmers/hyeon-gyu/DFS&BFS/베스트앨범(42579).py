
    
def solution(genres, plays):
    
    
    '''
    1. 장르별 토탈 재생수 구해서 장르 우선순위 구하기
    2. 장르별로 재생수 우선순위 매기기
    3. 장르별로 상위 두개씩만 
    
    '''
    
    answer = []
    playDic = {}  # {장르 : 총 재생 횟수}
    dic = {}      # {장르 : [(플레이 횟수, 고유번호)]}
    
    # 딕셔너리의 get함수 : key값으로 value를 리턴하는 기능 
    #                   + 에러발생을 막기 위해 key가 딕셔너리에 없다면 두 번째 인자를 리턴시킴.
    for i in range(len(genres)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]

    # 재생 횟수 내림차순으로 장르별 정렬
    genreSort = sorted(playDic.items(), key = lambda x: x[1], reverse = True)

    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key = lambda x: (-x[0], x[1]))
        print(dic[genre])
        answer += [idx for (play, idx) in dic[genre][:2]]
    
    return answer

