#!/usr/bin/env python
# coding: utf-8

# In[ ]:


HEADER_INFO = """""".strip()
SIDEBAR_INFO = """

<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://github.com/nxkyoungeun/AIFFEL_Hackathon">🪴Re미티드에디션 깃허브</a>
</div>

"""
UPCYCLING_INFO = """
<h2 class="font-title">Upcycling Brand for YOU!! </h2>
<p class="strong font-body">
<span class="d-block extra-info">(최근에 구매한 상품 정보를 입력하면 업사이클링 브랜드를 추천해드립니다! <br>무신사에 입점되어있는 업사이클링 브랜드 <strong>플리츠마마</strong>, <strong>누깍</strong>, <strong>오버랩업사이클</strong>,<br> <strong>119레오</strong>, <strong>큐클리프</strong>, <strong>카네이테이</strong>를 만나보세요.🤗)</span>
</p>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
🌱안녕하세요👋 <strong>Re미티드에디션팀</strong>입니다. 저희는 AIFFEL 에서 만나 자유주제 해커톤을 함께 진행하였습니다.
주제는 업사이클링 브랜드 추천시스템으로, 새로운 사용자의 최근 구매 정보를 입력하면 무신사에서 사용자와 비슷한 유저가 구매한 업사이클링 제품을 보여주는 것입니다.
추가적으로 가장 유사도가 높은 사용자가 구매한 업사이클링 브랜드 소개를 짧게 만나 보실 수 있습니다.
</p>
<p>
🏭이전부터 환경 파괴에 대한 문제 제기는 끊임없이 내어왔지만, 코로나바이러스 감염증이 발생한 이후 환경 파괴에 대한 심각성을 상기하게 되었습니다.
환경 파괴에 대한 원인 중 하나가 최신 유행하는 스타일의 저가 의류를 짧은 주기로 대량 생산해 판매하고, 유행이 끝나면 바로 폐기하는 시스템인 ‘패스트 패션’ 때문입니다.
<strong>오늘날 석유 다음으로 환경에 치명적인 오염원이 되었고, 세계에서 매년 1,000억 벌 이상의 의류가 만들어지며, 그중 약 33%인 330억 벌이 같은 해에 버려지고 있습니다.</strong>
</p>
<p>
♻️의류폐기물을 줄이는 방법 중 하나인 <strong>업사이클링</strong> 산업의 관심은 점점 증가하고 있습니다. 
하지만, 업사이클링 브랜드는 비교적 알려지지 못했습니다.
대중들에게 업사이클링과 국내브랜드를 알리기 위해 이 프로젝트를 기획했고, 해당 추천시스템을 통해 국내 업사이클링 브랜드를 알게되고 제품을 선택할 때 도움이 되기를 바랍니다.
</p>  


</div>
""".strip()

GOTOWEB = {
'누깍' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="http://nukak.kr/">👉Go Website!</a>
</div>
""",
'플리츠마마' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://pleatsmama.com/">👉Go Website!</a>
</div>
""",
'오버랩업사이클' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.overlab.kr/">👉Go Website!</a>
</div>
""",
'119레오' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.119reo.com/">👉Go Website!</a>
</div>
""",
'큐클리프' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://cueclyp.com/">👉Go Website!</a>
</div>
""",
'카네이테이' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.kaneitei.com/">👉Go Website!</a>
</div>
"""
    
    
}
