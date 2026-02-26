import streamlit as st
import requests

st.title("自動データ取得テスト（防御力UP版）")
st.write("ボタンを押すと、外部APIからデータを取得します。")

if st.button("データを取得する"):
    # ブロックされにくい別の無料API（猫の豆知識API）に変更
    url = "https://catfact.ninja/fact"
    
    try:
        # timeout=5 を設定し、5秒応答がなければ諦めるようにする
        response = requests.get(url, timeout=5)
        
        # HTTPステータスコードが200番台（成功）以外なら強制的にエラー扱いにする
        response.raise_for_status()
        
        # 成功した場合の処理
        data = response.json()
        fact_text = data["fact"]
        st.success(f"取得成功: {fact_text}")
        
    except requests.exceptions.RequestException as e:
        # 通信エラーやタイムアウトが起きた場合、アプリを落とさずここで受け止める
        st.error(f"データの取得に失敗しました。外部APIが応答していません。\n詳細: {e}")
