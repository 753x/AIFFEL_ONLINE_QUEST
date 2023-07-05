
# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 전요한
- 리뷰어 : 김소연

# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [O] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [O] 주석을 보고 작성자의 코드가 이해되었나요?
  > 함수가 작성된 부분과 호출에 대한 부분이 잘 구분되어서 작성되어 있었습니다.
  > sleep을 사용하여 출력에 2초 간격을 만들었다는 부분에 대한 설명이 잘 작성되어 있엇습니다.
- [O] 코드가 에러를 유발할 가능성이 없나요?
  > 네 입력값이 바뀌어도 잘 출력됩니다.
- [O] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  > 함수의 이름과 변수의 이름이 지어진 정황까지 정확히 기억하고 있었고 코드를 정확히 이해하고 작성하였음을 자세히 설명하였습니다.
- [O] 코드가 간결한가요?
  > 변수명과 함수명이 명확하게 작성되어 있고 반복적인 작업을 간단하게 처리할 수 있는 코드입니다.
# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
import time as t   #sleep함수를 쓰기 위해 import를 주고 t로 쓰기 쉽게 함

def fish_com(fish_list):  #컴프리헨션용 함수 작성
   return [f"{fish['이름']} is swimming at {fish['Speed']} m/s" for fish in fish_list]

def fish_gen(fish_list):  #제너레이터용 함수 작성
    for fish in fish_list:
      name = fish["이름"]
      speed = fish["Speed"]
      yield f"{name} is swimming at {speed} m/s"
      t.sleep(2)    #sleep함수를 이용하여 2초 간격으로 반복하게 함

fish_list = [     #fish 리스트 작성
    {"이름":"Nemo", "Speed":3 },
    {"이름":"Dory", "Speed":5}
]

print("Using Comprehension:")
fish_move = fish_com(fish_list)     #컴프리헨션 함수 호출
for movement2 in fish_move:
  print(movement2)
  t.sleep(2)

print("Using Generator:")
fish_generate = fish_gen(fish_list)     #제너레이터 함수 호출
for fish_movement in fish_generate:
  print(fish_movement) 
```

# 참고 링크 및 코드 개선
```python
def Comprehension_fish_movement(fish_list):  #함수명을 해당 함수가 동작하는 바를 더 명확하게 표현할 수 있도록 변경하였습니다.
   return [f"{fish['이름']} is swimming at {fish['Speed']} m/s" for fish in fish_list]

def generate_fish_movement(fish_list):  #함수명을 해당 함수가 동작하는 바를 더 명확하게 표현할 수 있도록 변경하였습니다.
    for fish in fish_list:
      name = fish["이름"]
      speed = fish["Speed"]
      yield f"{name} is swimming at {speed} m/s"
      t.sleep(2)    #sleep함수를 이용하여 2초 간격으로 반복하게 함




print("Using Comprehension:")
fish_move = fish_com(fish_list)     #컴프리헨션 함수 호출
for fish_movement2 in fish_move:    # fish_movement2로 변수명을 수정하여 컴프리헨션과 제너레이터의 변수명을 일관성 있게 변경.
  print(movement2)
  t.sleep(2)

print("Using Generator:")
fish_generate = fish_gen(fish_list)     #제너레이터 함수 호출
for fish_movement in fish_generate:
  print(fish_movement) 
```
