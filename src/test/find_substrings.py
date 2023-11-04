
my_list = ['apple', 'banana', 'cherry', 'date']
substring = 'an'

def find_substrings(lst, substring):
    result_list = []  # 결과를 담을 새로운 리스트를 초기화합니다.
    for element in lst:  # 주어진 리스트의 각 요소에 대해 반복합니다.
        if substring in element:  # 만약 현재 요소가 찾고자 하는 부분 문자열을 포함한다면,
            result_list.append(element)  # 그 요소를 결과 리스트에 추가합니다.
    return result_list

result_list = find_substrings(my_list, substring)
print(result_list)  # 출력: ['banana']
