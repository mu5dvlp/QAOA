# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    graphviz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# スクリプトをコピー
COPY maxCut.ipynb \ 
    commonLogic.py \
    /app/

# //ーーーーーーーーーーーーーーーーーーーーー
# pipをアップグレード
RUN pip install --upgrade pip

# 〜〜〜
# qiskitのインストール
RUN pip install qiskit qiskit_aer qiskit_optimization

# 回路図などの画像生成用
RUN pip install matplotlib
RUN pip install pylatexenc

# plot_state_qshpere用
RUN pip install seaborn

# 〜〜〜
RUN pip install scipy

# 〜〜〜
# jupyter notebookのインストール
RUN pip install notebook

# //ーーーーーーーーーーーーーーーーーーーーー
# Jupyter Notebookを起動するコマンドを指定
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


