import sys

t = int(sys.stdin.readline())

for i in range(t):

    result = 0

    str = list(sys.stdin.readline().rstrip())
    
    left_idx=0
    right_idx=len(str)-1
    
    while(left_idx<right_idx):
        if (str[left_idx]==str[right_idx]):
            left_idx+=1
            right_idx-=1
        else:
            if (str[left_idx+1:right_idx+1]==str[left_idx+1:right_idx+1][::-1]):
                result=1
                break
            elif (str[left_idx:right_idx]==str[left_idx:right_idx][::-1]):
                result=1
                break
            else:
                result=2
                break
    print(result)