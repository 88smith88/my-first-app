import streamlit as st
import requests

st.title("自動データ取得テスト")
st.write("ボタンを押すと、外部APIから最新のビットコイン価格を取得します。")

# ボタンを配置
if st.button("価格を取得する"):
    # アクセス先のAPIのURL（CoinDeskの無料API）
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    # URLにアクセスして情報を取得
    response = requests.get(url)
    
    # 正常に取得できたかチェック（200は成功の合図）
    if response.status_code == 200:
        # 取得したデータをプログラムで扱いやすい形（JSON）に変換
        data = response.json()
        # データの中から米ドル（USD）の価格だけを抜き出す
        price = data["bpi"]["USD"]["rate"]
        
        st.success(f"現在のビットコイン価格: {price} USD")
    else:
        st.error("データの取得に失敗しました。")
