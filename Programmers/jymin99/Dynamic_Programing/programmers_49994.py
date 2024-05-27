def solution(dirs):
    route=set() #set을 사용해 중복된 경로를 제거한다.
    x=0
    y=0
    #경로를 추가할 때는 무조건 작은 갚이 앞에 오도록 한다. 그래야 경로 비교해서 set으로 중복 제거 가능
    for d in dirs:
        if d=='U'and y<5:
            route.add(((x,y),(x,y+1)))
            y+=1
        elif d=='D'and y>-5:
            route.add(((x,y-1),(x,y)))
            y-=1
        elif d=='R'and x<5:
            route.add(((x,y),(x+1,y)))
            x+=1
        elif d=='L'and x>-5:
            route.add(((x-1,y),(x,y)))
            x-=1    
    return len(route)