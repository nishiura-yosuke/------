#左右のカラムに分けて配置する場合
import streamlit as st
import pandas as pd

# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_csv("リハビリ.csv")

# Streamlitアプリを作成する
def app():
    # アプリのタイトルを表示
    st.title("各種動画")

    # レイアウトを調整するためにカラムを使用する
    col1, col2 = st.columns(2)

    # 動画リストを表示する
    for index, row in data.iterrows():
        title = row["タイトル"]
        url = row["URL"]

        # 偶数番目の動画は左側のカラムに、奇数番目の動画は右側のカラムにボタンを配置する
        if index % 2 == 0:
            with col1:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                  st.video(url)
        else:
            with col2:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                  st.video(url)

if __name__ == "__main__":
    app()




def main():
     # アプリのタイトルを表示
    st.title("各種テキスト")
 
    # カラムの幅を設定
    col1, col2,col3= st.columns(3)
   
    # カラム1に要素を追加
    with col1:
    # 動画リストを表示する
        if st.button('テキスト'):
  # ボタンがクリックされた場合、対応するURLを開く
           st.markdown("[タイトル名](https://youtu.be/Wu6Q79qiZpI)")

   # カラム2に要素を追加
    with col2:
       if st.button('テキスト２'):
  # ボタンがクリックされた場合、対応するURLを開く
          st.markdown("[タイトル名２](https://youtu.be/Wu6Q79qiZpI)")
          
   # カラム3に要素を追加
    with col3:
       if st.button('テキスト3'):
  # ボタンがクリックされた場合、対応するURLを開く
          st.markdown("[タイトル名3](https://youtu.be/Wu6Q79qiZpI)")

if __name__ == "__main__":
    main()


#####
import numpy as np 

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

import time

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.balloons()

st.snow()

st.success('This is a success message!', icon="✅")

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


df1 = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df1)  # Same as st.write(df)

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
