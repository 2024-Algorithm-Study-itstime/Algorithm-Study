def solution(genres, plays):
    answer = []
    gen = {}
    
    #딕셔너리 형태로 만들고 genres : 스트리밍 횟수
    for i in range(len(genres)):
        gen[genres[i]] =0
        
    for i in range(len(genres)):
        gen[genres[i]] =   gen[genres[i]] + plays[i]
    

    sorted_gen = sorted(gen.items(), key=lambda item: item[1],reverse=True)
    print(gen,sorted_gen)
    for j in sorted_gen:
        g_idx = []

        for i in range(len(genres)):
            if  genres[i] == j[0]:
                g_idx.append(i)
        # print(g_idx)
        
        sorted_tracks = sorted(g_idx, key=lambda x: plays[x], reverse=True)
        answer.extend(sorted_tracks[:2])

    return answer
