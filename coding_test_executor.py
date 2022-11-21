from typing import List, Callable


def execute_test(solution: Callable, params: List):
    is_right = []
    for param in params:
        input = param[0]
        output = param[1]
        answer = solution(param)
        if answer == output:
            is_right.append(f'   입력값 〉 {input}\n    기댓값 〉 {output}\n 실행 결과 〉 \033[34m테스트를 통과하였습니다.\033[0m')
        else:
            is_right.append(f'   입력값 〉 {input}\n    기댓값 〉 {output}\n 실행 결과 〉 \033[31m실행한 결괏값 {answer}이 기댓값 {output}과 다릅니다.\033[0m')
    
    for n, res in enumerate(is_right):
        print(f'테스트 {str(n+1)}\n {res}\n {"-"*60}')
