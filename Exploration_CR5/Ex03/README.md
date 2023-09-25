# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 전요한
- 리뷰어 : 김소연


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 한국어 전처리를 통해 학습 데이터셋을 구축하였다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/0871123d-10a4-4ab7-8349-64c30ce74ed1)
        - 트랜스포머 모델을 구현하여 한국어 챗봇 모델 학습을 정상적으로 진행하였다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/bd74a528-7de4-4263-a0ab-0969d8022e8b)
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/5c72fd7b-d9ae-4cd3-abfe-11cca21ddc7b)
        - 한국어 입력문장에 대해 한국어로 답변하는 함수를 구현하였다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/adc4e896-5f7c-4bf4-b0df-7c8e6c2af1e0)
 
 

- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 학습률을 step에 따라 서서히 낮추어가면서 수렴하게 하는 스케쥴링 코드에 대한 설명이 잘 되어있었다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/cff108ab-8655-4015-8e5a-84e86fafc4b7)
        - 트랜스포머 모델의 각 레이어들을 선언하는 단계에서 레이어 내부의 코드가 각 어떤 역할을 수행하는지 잘 설명되어 있었다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/576de22d-2b07-406c-8046-80f2d36ecb9d)
 
 

        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 논문의 예시대로 학습을 진행하였을 때 정확도가 오히려 감소한다는 점을 파악하여 추가로 실험을 진행하였다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/59b4b705-2af6-404c-860f-0924572d29e6)
        - 파라미터를 조정하여 accuracy에서 유의미한 차이를 낸 것을 확인할 수 있었다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/07fc4e72-d535-4f96-8c10-6f169df1971b)
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/0305df8c-1356-4ba7-b11a-6819c21d6233)

 

       
- [x]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 추가로 진행한 학습과 이전 실험에 대한 회고가 잘 작성되어 있었다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/b49e98f6-2358-4b7d-8a99-4f7a74ff19bd)
 

        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 하드코딩을 하지않고 함수화, 모듈화가 가능한 부분은 함수를 만들거나 클래스로 짰는지
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화했는지
        - 각 인코더와 디코더 레이어를 구현하는 단게에서 반복적으로 사용되는 마스킹, attention 기능을 함수와 클래스 형태로 구현하여 코드를 간결하게 작성하였다.
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/ea1caf6d-89f1-4e65-8d18-1202451361d2)
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/5f454ee1-6d25-42c7-89ab-7706b49a58e8)
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/ca4629b3-a2ba-4719-b5ee-d83d98f69025)
            - 인코더
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/112afa09-ca67-4362-a8dd-595639846ba8)
            - 디코더
            - ![image](https://github.com/elliekim9881/AIFFEL_ONLINE_QUEST/assets/137244968/9b10840d-34b1-482b-b05d-1355a716c1d9)






# 참고 링크 및 코드 개선
- 파라미터를 조정하며 여러 결과를 알아본 시도는 좋았으나 loss와 accuracy라는 지표와 차이를 객관적인 지표로 알아보기 힘든 테스트결과만으로 나타내고 있기 때문에 NLP에서 쓰이는 평가지표인 BLEU, ROUGE, METEOR 등의 평가 지표를 계산
  해보았다면 더 다양한 분석과 새로운 상관관계를 찾는 데 도움이 되었을 것 같다.
```python
# BLEU(Bilingual Evaluation Understudy) : 기계 번역 결과와 사람이 직접 번역한 결과가 얼마나 유사한지 비교하여 번역에 대한 성능을 측정하는 방법입니다. 자연어처리에서 자주 사용되는 기본적인 평가 방법으로 n-gram(1~4)을 통해 순서쌍들이 얼마나 겹치는지에 대한 측정을 통해 생성한 캡션이 실제 참조 캡션의 유사도를 측정하는 방법입니다. 문법구조, 유의어들에 대한 고려가 부족하기 때문에 한계가 뜨렷한 방법이지만 여전히 많이 사용되는 방법입니다.
# METEOR(Metric for Evaluation of Translation with Explicit ORdering) : 기계 번역 출력의 평가를 위한 메트릭입니다. 이 메트릭은 유니그램 정밀도 및 재현율의 조화평균을 기반으로하며 정밀도 보다 재현율이 더 높습니다. 또한 표준 정확한 단어 일치와 함께 형태소 분석 및 동의어 일치와 같은 다른 메트릭에서 찾을 수 없는 여러 기능이 있습니다. 이 메트릭은 더 많이 사용되는 BLEU에서 발견된 일부 문제를 수정하도록 설계되었습니다. 또한 문장 또는 세그먼트 수준에서 인간의 판단과 좋은 상관관계를 생성합니다. 이것은 BLEU가 말뭉치 수준에서 상관관계를 찾는다는 점에서 BLEU 메트릭과 다릅니다.
#  ROUGE(Recall-Oriented Understudy for Gisting Evaluation) : 텍스트 요약 모델의 성능 평가 지표입니다. ROUGE는 텍스트 자동 요약, 기계 번역 등 자연어 생성 모델의 성능을 평가하기 위한 지표이며, 모델이 생성한 요약본 혹은 번역본을 사람이 미리 만들어 놓은 참조본과 대조해 성능 점수를 계산합니다.

import tensorflow as tf
import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import single_meteor_score
from rouge import Rouge

# 가정: model, test_data, tokenizer가 이미 정의되어 있음

def calculate_metrics(references, hypotheses):
    # BLEU
    bleu_scores = [sentence_bleu([ref], hyp) for ref, hyp in zip(references, hypotheses)]
    avg_bleu_score = np.mean(bleu_scores)
    
    # ROUGE
    rouge = Rouge()
    rouge_scores = rouge.get_scores(hypotheses, references, avg=True)
    
    # METEOR
    meteor_scores = [single_meteor_score(ref, hyp) for ref, hyp in zip(references, hypotheses)]
    avg_meteor_score = np.mean(meteor_scores)
    
    print(f'Average BLEU score: {avg_bleu_score:.2f}')
    print(f'ROUGE scores: {rouge_scores}')
    print(f'Average METEOR score: {avg_meteor_score:.2f}')

def generate_predictions(model, data, tokenizer):
    predictions = []
    for example in data:
        # 모델을 사용하여 예측 생성 (여기서는 간단한 예시로 처리)
        prediction = model(example)
        # 토큰을 텍스트로 변환
        prediction_text = tokenizer.decode(prediction, skip_special_tokens=True)
        predictions.append(prediction_text)
    return predictions

# 테스트 데이터에서 예측 생성
hypotheses = generate_predictions(model, test_data, tokenizer)

# 참조 데이터 준비 (테스트 데이터의 실제 출력)
references = [...]  # 이 부분을 실제 데이터에 맞게 채우세요

# 평가 지표 계산
calculate_metrics(references, hypotheses)

```

- NLP 평가 지표 검색 (https://blog.testworks.co.kr/nlp-generation-evaluation/)
- BLEU, ROUGE, METEOR 코드생성 ( chat GPT )
