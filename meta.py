#!/usr/bin/env python
# coding: utf-8

# In[ ]:


HEADER_INFO = """""".strip()
SIDEBAR_INFO = """

<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://github.com/nxkyoungeun/AIFFEL_Hackathon">πͺ΄Reλ―Έν°λμλμ κΉνλΈ</a>
</div>

"""
UPCYCLING_INFO = """
<h2 class="font-title">Upcycling for YOU!! </h2>
<p class="strong font-body">
<span class="d-block extra-info">(μ΅κ·Όμ κ΅¬λ§€ν μν μ λ³΄λ₯Ό μλ ₯νλ©΄ μμ¬μ΄ν΄λ§ λΈλλλ₯Ό μΆμ²ν΄λλ¦½λλ€! <br>λ¬΄μ μ¬μ μμ λμ΄μλ μμ¬μ΄ν΄λ§ λΈλλ <strong>νλ¦¬μΈ λ§λ§</strong>, <strong>λκΉ</strong>, <strong>μ€λ²λ©μμ¬μ΄ν΄</strong>,<br> <strong>119λ μ€</strong>, <strong>νν΄λ¦¬ν</strong>, <strong>μΉ΄λ€μ΄νμ΄</strong>λ₯Ό λ§λλ³΄μΈμ.π€)</span>
</p>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
π±μλνμΈμπ <strong>Reλ―Έν°λμλμν</strong>μλλ€. μ ν¬λ AIFFEL μμ λ§λ μμ μ£Όμ  ν΄μ»€ν€μ ν¨κ» μ§ννμμ΅λλ€.
μ£Όμ λ μμ¬μ΄ν΄λ§ λΈλλ μΆμ²μμ€νμΌλ‘, μλ‘μ΄ μ¬μ©μμ μ΅κ·Ό κ΅¬λ§€ μ λ³΄λ₯Ό μλ ₯νλ©΄ λ¬΄μ μ¬μμ μ¬μ©μμ λΉμ·ν μ μ κ° κ΅¬λ§€ν μμ¬μ΄ν΄λ§ μ νμ λ³΄μ¬μ£Όλ κ²μλλ€.
μΆκ°μ μΌλ‘ κ°μ₯ μ μ¬λκ° λμ μ¬μ©μκ° κ΅¬λ§€ν μμ¬μ΄ν΄λ§ λΈλλ μκ°λ₯Ό μ§§κ² λ§λ λ³΄μ€ μ μμ΅λλ€.
</p>
<p>
π­μ΄μ λΆν°Β νκ²½Β νκ΄΄μΒ λνΒ λ¬Έμ Β μ κΈ°λΒ λμμμ΄Β λ΄μ΄μμ§λ§,Β μ½λ‘λλ°μ΄λ¬μ€Β κ°μΌμ¦μ΄Β λ°μνΒ μ΄νΒ νκ²½Β νκ΄΄μΒ λνΒ μ¬κ°μ±μΒ μκΈ°νκ²Β λμμ΅λλ€.
νκ²½Β νκ΄΄μΒ λνΒ μμΈΒ μ€Β νλκ°Β μ΅μ Β μ ννλΒ μ€νμΌμΒ μ κ°Β μλ₯λ₯ΌΒ μ§§μΒ μ£ΌκΈ°λ‘Β λλΒ μμ°ν΄Β νλ§€νκ³ ,Β μ νμ΄Β λλλ©΄Β λ°λ‘Β νκΈ°νλΒ μμ€νμΈΒ βν¨μ€νΈΒ ν¨μβΒ λλ¬Έμλλ€.
<strong>μ€λλ Β μμ Β λ€μμΌλ‘Β νκ²½μΒ μΉλͺμ μΈΒ μ€μΌμμ΄Β λμκ³ ,Β μΈκ³μμΒ λ§€λΒ 1,000μ΅Β λ²Β μ΄μμΒ μλ₯κ°Β λ§λ€μ΄μ§λ©°,Β κ·Έμ€Β μ½Β 33%μΈΒ 330μ΅Β λ²μ΄Β κ°μΒ ν΄μΒ λ²λ €μ§κ³ Β μμ΅λλ€.</strong>
</p>
<p>
β»οΈμλ₯νκΈ°λ¬Όμ μ€μ΄λ λ°©λ² μ€ νλμΈ <strong>μμ¬μ΄ν΄λ§</strong> μ°μμ κ΄μ¬μ μ μ  μ¦κ°νκ³  μμ΅λλ€. 
νμ§λ§, μμ¬μ΄ν΄λ§ λΈλλλ λΉκ΅μ  μλ €μ§μ§ λͺ»νμ΅λλ€.
λμ€λ€μκ² μμ¬μ΄ν΄λ§κ³Ό κ΅­λ΄λΈλλλ₯Ό μλ¦¬κΈ° μν΄ μ΄ νλ‘μ νΈλ₯Ό κΈ°ννκ³ , ν΄λΉ μΆμ²μμ€νμ ν΅ν΄ κ΅­λ΄ μμ¬μ΄ν΄λ§ λΈλλλ₯Ό μκ²λκ³  μ νμ μ νν  λ λμμ΄ λκΈ°λ₯Ό λ°λλλ€.
</p>  


</div>
""".strip()

GOTOWEB = {
'λκΉ' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="http://nukak.kr/">πGo Website!</a>
</div>
""",
'νλ¦¬μΈ λ§λ§' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://pleatsmama.com/">πGo Website!</a>
</div>
""",
'μ€λ²λ©μμ¬μ΄ν΄' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.overlab.kr/">πGo Website!</a>
</div>
""",
'119λ μ€' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.119reo.com/">πGo Website!</a>
</div>
""",
'νν΄λ¦¬ν' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://cueclyp.com/">πGo Website!</a>
</div>
""",
'μΉ΄λ€μ΄νμ΄' : """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.kaneitei.com/">πGo Website!</a>
</div>
"""
    
    
}
