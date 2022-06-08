#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
# import textwrap

# import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
# import operator

import nltk
from nltk.tokenize import TreebankWordTokenizer

from sklearn.feature_extraction.text import TfidfVectorizer

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


import meta
import introduce


# In[ ]:


@st.cache()

def simil_brand(user, new_feature):

#     raw = pd.read_csv('/Users/mac/AIFFEL/hackathon/new_musinsa(upcycling).csv', engine='python')
#     orginal_data_size = len(raw)
#     # rating 3점 이상만 사용
#     raw = raw[raw['ratings']>=2]
#     filtered_data_size = len(raw)
#     cols = ['color', 'contents', 'category', 'ratings', 'gender', 'price', 'style']
#     raw['features'] = raw[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
#     raw.drop(['Unnamed: 0', 'color', 'contents', 'category', 'ratings', 'gender', 'price', 'style'], axis=1, inplace=True)
    raw = pd.read_csv('asset/streamlit_data.csv')

        
    # 데이터 마지막행에 추가
    new_data = {'user' : user, 'features' : new_feature}
    new_raw = raw.append(new_data, ignore_index = True)
    
    # 토큰화 & 벡터화
    tb_tokenizer = TreebankWordTokenizer()

    tfidf = TfidfVectorizer(tokenizer=tb_tokenizer.tokenize)

    tfidf_matrix = tfidf.fit_transform(new_raw['features'])
    
    # 코사인 매트릭스
    cosine_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    np.round(cosine_matrix, 4)

    # brand 와 id 를 매핑할 dictionary 를 생성
    brand2id = {}
    for i, c in enumerate(new_raw['brand']): brand2id[i] = c

    # id 와 brand 를 매핑할 dictionary 를 생성
    id2brand = {}
    for i, c in brand2id.items(): id2brand[c] = i
        
    # user 와 id 를 매핑할 dictionary 를 생성
    user2id = {}
    for i, c in enumerate(new_raw['user']): user2id[i] = c

    # id 와 user 를 매핑할 dictionary 를 생성
    id2user = {}
    for i, c in user2id.items(): id2user[c] = i

    idx = id2user[user]
    sim_scores = [(i, c) for i, c in enumerate(cosine_matrix[idx]) if i != idx] # 자기 자신을 제외한 영화들의 유사도 및 인덱스를 추출
    
    # 유사도가 높은 순수대로 정렬
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True)
    
    # 만들어 둔 딕셔너리에 적용해 user id 와 brand 확인
    sim_scores = [(user2id[i], brand2id[i], score) for i, score in sim_scores[0:3]]
    
    # 결과 문구 작성
    sim_user = f"당신과 비슷한 유저는 {sim_scores[0][0], sim_scores[1][0], sim_scores[2][0]} 입니다."
    
    #item1 = raw[(raw.user == sim_scores[0][0]) & (raw.up_check == 1)]['url']
    item1 = raw[(raw.user == sim_scores[0][0]) & (raw.up_check == 1)]["url"].tolist()[0]
    item2 = raw[(raw.user == sim_scores[1][0]) & (raw.up_check == 1)]['url'].tolist()[0]
    item3 = raw[(raw.user == sim_scores[2][0]) & (raw.up_check == 1)]['url'].tolist()[0]
    
    brand_1 = sim_scores[0][1]
    
    sim_item1 = f"당신과 비슷한 유저인 {sim_scores[0][0]} 이(가) 구매한 업사이클링 아이템은 {sim_scores[0][1]} {item1} 입니다."
    sim_item2 = f"당신과 비슷한 유저인 {sim_scores[1][0]} 이(가) 구매한 업사이클링 아이템은 {sim_scores[1][1]} {item2} 입니다."
    sim_item3 = f"당신과 비슷한 유저인 {sim_scores[2][0]} 이(가) 구매한 업사이클링 아이템은 {sim_scores[2][1]} {item3} 입니다."

    return sim_user, sim_item1, sim_item2, sim_item3, brand_1

 

# In[ ]:


def main():
    st.set_page_config(
        page_title="Upcycling for YOU",
        page_icon="🌏",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    col1, col2 = st.columns([6, 4])
    with col2:
        image_ = Image.open("/asset/여섯001.png")
        st.image(image_, width=400)
    
        st.markdown(meta.SIDEBAR_INFO, unsafe_allow_html=True)

        with st.expander("Where did this story start?", expanded=True):
             st.markdown(meta.STORY, unsafe_allow_html=True)

    with col1:
        st.markdown(meta.HEADER_INFO, unsafe_allow_html=True)

        st.markdown(meta.UPCYCLING_INFO, unsafe_allow_html=True)
        
        new_user = st.text_input("Text your name", 'HAPPY')
        new_color = st.selectbox("Choose color", index=0, options=["블랙", "그레이", "블루", 
                                                                   "화이트", "네이비", "그린", 
                                                                   "카키", "베이지", "아이보리", 
                                                                  "멀티", "기타"])
        new_contents = st.multiselect('Select contents in multi selectbox',
                                ['면', '폴리에스터', '나일론', '레이온', '폴리우레탄', '울', '아크릴', '리사이클폴리에스터', '코듀라', 
                                 '레더', '아라미드', 'None'
                                ])
        new_cont_str = ' '.join(s for s in new_contents)
        new_category = st.selectbox("Choose category", index=0, options=["상의", "하의", "셋업", "가방", "모자", "파우치"])
        new_rating = st.selectbox("Choose rating", index=0, options=["5", "4", "3"])
        new_gender = st.selectbox("Choose gender", index=0, options=["남자", "여자"])
        new_price = st.text_input("Text price(원) (ex : 54320)", "10000")
        new_style = st.selectbox("Pattern(No : 0, Yes : 1)", index=0, options=["0", "1"])
        
        items = new_user + ' ' + new_color + ' ' + new_cont_str + ' ' + new_category + ' ' + new_rating + ' ' + new_gender + ' ' + new_price + ' ' + new_style
        rcm_feature = new_color + ' ' + new_cont_str + ' ' + new_category + ' ' + new_rating + ' ' + new_gender + ' ' + new_price + ' ' + new_style
        
        entered_items = st.empty()
        
    recipe_button = st.button('Get Recommendation!')
    
    st.markdown(
         "<hr />",
     unsafe_allow_html=True
     )
    if recipe_button:
        
        entered_items.markdown("**Generate recommendation for:** " + items)
        with st.spinner("Generating recommendation..."):
            
            if not len(items) > 2:
                entered_items.markdown(
                    "**Please select FULL info**"
                )
            else:
            
                rcm_u, rcm1, rcm2, rcm3, up_brand1 = simil_brand(new_user, rcm_feature)
                
                r1, r2 = st.columns([5, 3])

                with r2:
                    st.markdown(
                        " ".join([
                            "<div class='r-text-result'>",
                            "<div class='title'>",
                            f"<h2 class='font-title text-bold'>{up_brand1}</h2>",
                            "</div>",
                            "</div>"
                        ]),
                        unsafe_allow_html=True
                    )
                    #st.write(up_brand1)
                    info = introduce.brand_info[up_brand1]
                    st.write(info)
                    st.markdown(meta.GOTOWEB[up_brand1], unsafe_allow_html=True)

                with r1:
                
                    st.markdown(rcm_u)
                    st.markdown(rcm1)
                    st.markdown(rcm2)
                    st.markdown(rcm3)
                        


# In[ ]:


if __name__ == '__main__':
    main()

