import sys
sys.stdin = open("input.txt")


T = 10

def flatten(N,numbers):

    #  테스트 케이스 틀릴때는 N까지의 범위로 함 하지만 실질적으로 한번더 실행해 주어야 되는 것이 맞음
    for tn in range(N+1):
        # 최대,최소 값과 각각의 idx 초기값 선언
        max_height = 0
        min_height = 100
        max_idx = 0
        min_idx = 0
        # 최소값과 최대값 구하는 반복문
        for i in range(len(numbers)):
            if numbers[i] > max_height:
                max_height = numbers[i]
                max_idx = i

            if numbers[i] < min_height:
                min_height = numbers[i]
                min_idx = i

        # 최대값에서 1빼고 최소값에서 1더하는 과정
        numbers[max_idx] = numbers[max_idx] - 1
        numbers[min_idx] = numbers[min_idx] + 1

        #  만약 높이가 같아진다면 0으로 종료
        if max_height == min_height:
            return 0

    return max_height - min_height





for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result = flatten(N,numbers)
    print("#{} {}".format(tc,result))

