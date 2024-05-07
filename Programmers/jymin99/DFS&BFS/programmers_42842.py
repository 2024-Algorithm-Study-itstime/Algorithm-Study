#내풀이
def solution(brown, yellow):
    total=brown+yellow #모든 칸수의 합을 total 에 저장
    for height in range(1,total): #height를 반복문으로 돌림
        if total%height==0: #전체 타일수를 나눠떨어지게하는 height  거르기
            width=total/height 
            if yellow==(height-2)*(width-2): #그 중 조건을 만족시키는 width고르기
                return[width,height]
            

#더 나은 물이
#수학 공식 그대로 넣기
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
