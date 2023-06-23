import streamlit as st
import random


st.title('各種教育ツール')
st.subheader('各種項目にはサイドから選択してください。')
st.caption('スマートフォンの場合は、左上の＞を押してください。')

st.title('今日の運勢')
st.write('おみくじボタンを押して、おみくじの結果を表示します。')

if st.button('おみくじ'):
    results = ['大吉', 'いい感じ、知らんけど', 'なんじゃこりゃ〜', '奇跡が起こるかも']
    result = random.choice(results)
    st.write('結果：', result)