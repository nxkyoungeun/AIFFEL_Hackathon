# 1) feature 묶은 후, TF-IDF 벡터화 후, 머신러닝

|LogisticRegression|<img width="500" alt="스크린샷 2022-06-08 오전 11 40 30" src="https://user-images.githubusercontent.com/97087253/172519518-e5a165fd-bab2-4687-8caa-6057805c81eb.png">|f1 score : 0.55|
|----|----|----|
|DecisionTree|<img width="500" alt="스크린샷 2022-06-08 오전 11 36 11" src="https://user-images.githubusercontent.com/97087253/172519063-e4dc6483-5d5f-412f-a617-400f98a394fb.png">|f1 score : 0.39|
|RandomForest|<img width="500" alt="스크린샷 2022-06-08 오전 11 38 07" src="https://user-images.githubusercontent.com/97087253/172519269-a1870c96-3a86-4794-b909-104ca01d05e5.png">|f1 score : 0.45|
|GradientBoosting|<img width="500" alt="스크린샷 2022-06-08 오전 11 39 11" src="https://user-images.githubusercontent.com/97087253/172519382-fc7a82a1-83d4-4b8d-af8d-7acbfd8ea847.png">|f1 score : 0.45|

# 2) 컬럼 통합 X, 라벨링 & price 정규화 후
|LogisticRegression|<img width="500" alt="스크린샷 2022-06-08 오전 11 45 40" src="https://user-images.githubusercontent.com/97087253/172520575-af9fa442-9ead-414a-83ea-826b3901a9d6.png">|f1 score : 0.55|
|----|----|----|
|RandomForest(Standard Scaler)|<img width="500" alt="스크린샷 2022-06-08 오전 11 47 22" src="https://user-images.githubusercontent.com/97087253/172520741-e5d01ebd-f81f-43cf-b2df-8f479125bcc9.png">|f1 score : 0.57|

# 3)price 컬럼 MinMax Scaler 사용하여 정규화
|LogisticRegression(MinMax Scaler)|<img width="500" alt="스크린샷 2022-06-08 오전 11 57 25" src="https://user-images.githubusercontent.com/97087253/172521953-1c2e3ebf-7712-4aeb-ac56-e497f90047f6.png">|f1 score : 0.33|
|----|----|----|


