from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

# Streamlitページの幅を調整する
st.set_page_config(page_title="StreamlitでPygwalkerを使う", layout="wide")

# PyGWalkerとStreamlitの通信を確立する
init_streamlit_comm()

# タイトルを追加
st.title("StreamlitでPygwalkerを使う")


# PyGWalkerのレンダラーのインスタンスを取得する。このインスタンスをキャッシュすることで、プロセス内メモリの増加を効果的に防ぐことができます。
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv(
        "https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv"
    )
    # アプリをパブリックに公開する場合、他のユーザーがチャートの設定ファイルに書き込めないように、デバッグパラメータをFalseに設定する必要があります。
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)


renderer = get_pyg_renderer()

# データ探索インターフェースをレンダリングする。開発者はこれを使用してドラッグアンドドロップでチャートを作成できます。
renderer.render_explore()
