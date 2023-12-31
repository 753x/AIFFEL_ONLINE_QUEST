# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 전요한
- 리뷰어 : 조대희


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭


    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
    - 주석을 보고 코드 이해가 잘 되었는지 확인


<img src="img/Screenshot 2023-09-11 at 3.20.41 PM.png">



- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” ”새로운 시도 또는 추가 실험을 수행”해봤나요?**  
    - 예측값들을 시각화한 결과에서 색의 좌우반전이 일어나는 현상을 개선하기 위해 시도하였다.
    - 기록 부재

        
- [ ]  **4. 회고를 잘 작성했나요?**
    - 회고 부재
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 하드코딩을 하지않고 함수화, 모듈화가 가능한 부분은 함수를 만들거나 클래스로 짰는지
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화했는지

    <img src="img/Screenshot 2023-09-11 at 3.19.09 PM.png">
        


# 참고 링크 및 코드 개선
```
데이터셋 내려받기:

데이터셋을 분할할 때, 특정 비율로 나누는 것은 좋은 방법이지만, 데이터셋이 변경되면 이 비율이 의도하지 않은 결과를 가져올 수 있습니다. 데이터의 개수를 확인하여 분할하는 것이 더 안전할 수 있습니다.
데이터 전처리:

shuffle 함수를 사용할 때, buffer size를 전체 데이터셋 크기와 동일하게 설정하는 것이 좋습니다. 그러나 이렇게 하면 메모리 문제가 발생할 수 있기 때문에 충분한 버퍼 크기를 설정하는 것이 중요합니다.
데이터 증강(augmentation)을 고려하면 모델의 일반화 성능이 향상될 수 있습니다.
모델 설계:

VGG16은 이미지 분류 작업에 매우 효과적이지만, 현재 코드에서는 전이 학습(transfer learning)을 사용하고 있습니다. 따라서 다른 사전 훈련된 모델도 고려해볼 수 있습니다.
모델의 복잡성을 줄이기 위해 Dense layer의 뉴런 수를 조정할 수 있습니다.
모델 학습:

EarlyStopping이나 ModelCheckpoint와 같은 콜백(callback)을 사용하여 과적합을 방지하고 최적의 모델을 저장할 수 있습니다.
모델 성능 평가:

predictions = np.argmax(predictions, axis=1) 이 코드는 두 번 반복되었습니다. 중복된 코드를 제거하는 것이 좋습니다.
이미지 시각화 부분에서 이미지를 [0, 1] 범위로 조정하는 코드는 VGG16의 전처리 과정과 충돌할 수 있으므로 주의가 필요합니다.
32개의 이미지에 대한 정확도 계산 부분은 더 간결하게 작성할 수 있습니다
