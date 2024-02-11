# pygwalker_demo
pygwalker_demo

## 実行方法

- Dockerイメージのビルド(作成時に1度だけ実行)
```
docker image build -t pygwalker_demo .
```
- Dockerコンテナの起動
```
docker container run -it --rm -p 8501:8501 pygwalker_demo bash
```
- Streamlitの起動
コンテナ内で
```
streamlit run home.py
```
実行したら、以下にアクセス。

(http://localhost:8501)