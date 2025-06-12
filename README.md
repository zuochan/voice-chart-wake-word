# Wake Word 検出セットアップガイド

このプロジェクトは、Python を用いてウェイクワード検出（Wake Word Detection）を行うために **`openwakeword`** および **`pyaudio`** を使用します。

## 動作環境

**-** **Python バージョン:** 3.7 以上

**-** **必要な Python パッケージ:**

**  **-** [**`openwakeword`**](**https://pypi.org/project/openwakeword/**)**

**  **-`pyaudio`

## 任意の Linux 追加パッケージ

ノイズ抑制機能を使用する場合、Linux 環境では以下のパッケージを追加でインストールしてください：

```bash
sudo apt install libspeexdsp-dev
```

ノイズ抑制を有効にするには、**speexdsp_ns** の **.whl** ファイルをインストールします：

```bash
pip install /path/to/speexdsp_ns.whl
```

※ **/path/to/** は実際のファイルのパスに置き換えてください。

## インストール手順

```bash
# 必要な Python パッケージをインストール
pip install openwakeword pyaudio

# （Linux 環境のみ）ノイズ抑制に必要なパッケージをインストール
sudo apt install libspeexdsp-dev

# （任意）ノイズ抑制モジュールをインストール
pip install /path/to/speexdsp_ns.whl
```

## カスタムウェイクワードの作成

[**openWakeWord**](**https://github.com/dscripka/openWakeWord**) 用の **カスタムウェイクワードモデル** を簡単に作成できる Google Colab ノートブックを利用して、独自のカスタムウェイクワードが作成可能です。

以下のノートブックを使えば、ブラウザ上で音声データの準備からモデルのトレーニング・ダウンロードまでを一括で行うことができます。

トータルで1〜2時間ほど要します。

🔗 **Colab ノートブック** ** **

**[**👉 カスタムウェイクワード作成ノートブック（Google Colab）**](**https://colab.research.google.com/drive/1qf_2nqbiFh_5OqB_x0VjWFRFDGLf5Tas?usp=sharing**)**


## 🔧 カスタムモデルの配置と使用

トレーニング後に生成される **`.onnx`** モデルファイルは、**`my_custom_model`** フォルダに保存されます。

**1.** そのファイル（例：**`start.onnx`**）を、wake word 検出スクリプトがあるフォルダに移動します。

**2.**`wake_word.py` **内の以下の引数設定を変更します：**

```python


parser.add_argument(


**    **"--model_path",


**    **help="The path of a specific model to load",


**    **type=str,


**    **default="./<ファイル名>.onnx",


**    **required=False


)
```



---
