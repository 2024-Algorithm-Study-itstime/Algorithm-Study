def solution(n, times):
    
    # 최소 시간, 최대 시간
    start = 1
    end = max(times)*n
    
    while(start<=end):
        mid = (start+end)//2
        cnt =0
        for t in times:
            cnt += mid//t
            #모 든 심사관을 거치지 않고 모든 인원 심사 완료했을면 break
            if cnt >=n: 
                break
        if cnt >= n:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans