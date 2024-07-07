# 実行方法
## VSCodeの場合
### 1. ライブラリのインポート
以下を実行します

```bash
pip install qiskit qiskit_aer qiskit_optimization qiskit_ibm_runtime

pip install matplotlib
pip install pylatexenc

pip install scipy

pip install notebook
```

### 2. VSCodeで開く
main.ipynbを開いてください。そのまま実行できます。

## Dockerの場合
### 1. ビルドする

```bash
docker build -t qaoa .
```

### 2. コンテナを実行する

```bash
docker run -it -p 8888:8888 qaoa
```

### 3. ブラウザで開く
コンテナ実行後、10秒ちょっと待つと以下の様な出力が確認できます。

```bash
Jupyter Server 2.14.1 is running at:
    http://{毎回異なるホスト}:8888/tree?token={毎回異なるトークン}
        http://127.0.0.1:8888/tree?token={毎回異なるトークン}
```

ここで、「http://〜」で始まるどちら1行をコピーして、ブラウザのアドレスバーから検索します。
すると、jupyter notebookが開きます。
あとは、maxCut.ipynbを開き、実行します。

# 補足
一応、実機でも試してみました。(maxCut_RemoteJob.ipyenb)
しかし、デコヒーレンスのせいか全く正しい計算結果が得られませんでした。
試してみるのも良いですが、期待される結果は得られないことに注意してください。
