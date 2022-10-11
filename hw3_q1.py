def solution(list, num):
    a=0
    b=0

    for a in range(len(list)):
        for b in range(a+1, len(list)):
            if list[b] == num - list[a]:
                   a = list[a]
                   b = list[b]
            else:
                print("None")
            return a, b

numbers = [0, 21, 78, 19, 90, 13]
print(solution(numbers, 21))
print(solution(numbers, 25))
