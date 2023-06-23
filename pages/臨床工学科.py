#左右のカラムに分けて配置する場合
import streamlit as st
import pandas as pd

# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_csv("臨床工学科.csv")

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
        if st.button('各種リンク'):
  # ボタンがクリックされた場合、対応するURLを開く
           st.markdown("[日本工学技士会HP](https://ja-ces.or.jp/for-students/clinical-engineer/)")

   # カラム2に要素を追加
    with col2:
       if st.button('各種マニュアル'):
  # ボタンがクリックされた場合、対応するURLを開く
          st.markdown("[タイトル名２](https://youtu.be/Wu6Q79qiZpI)")
          
   # カラム3に要素を追加
    with col3:
       if st.button('テキスト3'):
  # ボタンがクリックされた場合、対応するURLを開く
          st.markdown("[タイトル名3](https://youtu.be/Wu6Q79qiZpI)")

if __name__ == "__main__":
    main()
