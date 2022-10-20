![header](https://capsule-render.vercel.app/api?type=waving&color=9ACB34&height=300&section=header&text=🪴업사이클링%20브랜드%20추천🪴&fontSize=70&)

[♻️](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%ED%99%98%EA%B2%BD.md)<br>

## 목차
[1. 팀원 구성 및 역할](#팀원-구성-및-역할)<br>
[2. 프로젝트 배경](#프로젝트-배경)<br>
[3. 프로젝트 소개](#프로젝트-소개)<br>
[4. 추천시스템](#추천시스템)<br>
5. 회고
***
### 팀원 구성 및 역할
* 팀명 : Re미티드에디션♻️
* 팀원 & 역할
  | 팀원 | 역할 |
  | :---: | :---: |
  | 노경은 | 데이터 전처리, 모델 구성, 웹페이지 구성 |
  | 유동린 | 데이터 수집, 데이터 시각화 |
  | 우성아 | 참고 자료 수집 |
* 해커톤 기간 : 2022. 05. 03 ~ 2022. 06. 09
* **프로젝트 정리 PPT** [Go!💻](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%89%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%BC%E1%84%87%E1%85%B3%E1%84%85%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%E1%84%8E%E1%85%AE%E1%84%8E%E1%85%A5%E1%86%AB.pdf)

#

### 프로젝트 배경
> 환경문제가 대두되고 있는 요즘 업사이클링에 대한 대중들의 관심은 높아졌으나 업사이클링 브랜드는 비교적 알려지지 못했다.  
업사이클링 브랜드 중 가장 유명한 브랜드는 스위스 브랜드인 '[프라이탁](https://ko.wikipedia.org/wiki/%ED%94%84%EB%9D%BC%EC%9D%B4%ED%83%81)'이라고 생각한다.  
국내에도 이와 비슷한 다양한 브랜드가 존재한다. 대중들에게 업사이클링과 국내브랜드를 알리기 위해 이 프로젝트를 기획했다.  
대중들이 해당 추천시스템을 통해 국내 업사이클링 브랜드를 알게되고 제품을 선택할 때 도움이 되기를 바란다.

#

### 프로젝트 소개
1. [데이터 수집](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91%20%EA%B3%BC%EC%A0%95.md)<br>
- 업사이클링 브랜드별로 표시하고 있는 데이터 형식들이 다르기 때문에 스크래핑 후 전처리 작업이 더 오래 걸릴 것이라 예상했다.
- 의류 이커머스인 무신사에서 업사이클링 아이템을 구매한 사용자들의 구매내역을 수집하였다.
2. 선정 대상
- 업사이클링 아이템은 가방류, 의류, 모자로 한정한다.
- 위 아이템을 구매한 사용자의 구매후기를 수집했다.
3. 컬럼 소개
- 사이트, 사용자이름(ID), 색상, 소재, 종류, 별점, 성별(구매자), 가격, 무늬, 업사이클링브랜드(0과 1, 이름), 웹사이트주소
4. [데이터 분석](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%8B%9C%EA%B0%81%ED%99%94.md)<br>

5. [추천시스템 종류(시도한 것들)](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%EB%AA%A8%EB%8D%B8%20%EC%8B%9C%EB%8F%84%ED%95%9C%EA%B2%83/%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%A2%85%EB%A5%98(%EC%8B%9C%EB%8F%84%ED%95%9C%20%EA%B2%83%EB%93%A4).md)<br>
- 분류 머신러닝
- keras Sequential(softmax) 분류 
- 뉴럴 네트워크 임베딩
- 코사인유사도(Word2Vec)

#

### 추천시스템
1. [데이터 전처리](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%84%EC%B2%98%EB%A6%AC.md)<br>
- **데이터 전처리 방법**
  - 색상  
    - 데이터 전체 색상 개수 39개를 👉🏻 11개로 줄였다
  - 소재  
    - 데이터 전체 소재 개수 76개를 👉🏻 62개로 줄였다
2. 모델
- **[사용한 모델 코드](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%E1%84%8F%E1%85%A9%E1%84%89%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%B2%E1%84%89%E1%85%A1%E1%84%83%E1%85%A9(TF-IDF)01.ipynb)<br>**
  - TF-IDF 벡터화
  - 코사인 유사도
  - [결과](https://github.com/nxkyoungeun/AIFFEL_Hackathon/blob/main/%EC%BD%94%EC%82%AC%EC%9D%B8%EC%9C%A0%EC%82%AC%EB%8F%84(TF-IDF).md)

3. 추천시스템 결과물  
- 사용 툴 : Streamlit <br>
[<img width="300" alt="image" src="https://user-images.githubusercontent.com/96903792/172726731-7fdbe0f7-4551-4c28-8925-bb937ea0dd5a.png">
](https://streamlit.io/)<br>

***

<img width="650" alt="스크린샷 2022-06-08 오후 5 33 28" src="https://user-images.githubusercontent.com/97087253/172570960-f16f094e-619f-4fad-a758-89e3b64f427e.png">

- **결과페이지 스트림릿 설명**  
a. 새로운 사용자의 최근 구매 정보를 입력 
    구매 정보: 색상, 소재, 종류, 별점, 성별, 가격, 무늬여부  
     -> 데이터 마지막 행에 새로운 사용자 구매 정보를 추가  
b. 모델 실행  
c. 결과 도출: 업사이클링 브랜드 추천 or 비슷한 유저가 구매한 업사이클링 제품 추천  
d. (추가로 발전시켜야 할 부분) 결과에 대한 만족도를 물어본다. -> 만족함 or 불만족을 선택한다. -> (만족함을 선택한 사람 만)추천한 업사이클링 브랜드를 데이터에 추가한다. -> 새로운 유저의 정보를 얻을 수 있다.  

# [🌍Upcycling for You](https://share.streamlit.io/nxkyoungeun/aiffel_hackathon/main/app.py)<br>


![header](https://capsule-render.vercel.app/api?type=waving&color=9ACB34&height=300&section=footer&fontSize=90&)


