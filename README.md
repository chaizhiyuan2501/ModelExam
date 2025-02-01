# Djangoの Modelの利用の練習

## 📌 概要
このプロジェクトは、Django の **Modelにデータを挿入して取り出す** を学ぶための練習用アプリケーションです。

本プロジェクトは、以下の Udemy コースのセッション7をベースに実装しました：
📚 [Python + Django5 Djangoを基礎から応用まで、アプリケーション開発マスターpython付き](https://www.udemy.com/share/103OHY3@5JdSpwpJtBk6FXDdLoQeB-D1g_nt31JH7eSso0Ld1otnAfjP6jSbJjPZHRQXrwCRsA==/)

**学習ポイント**
- Django の **Model定義作成方法**
- **モデルフィールドの型の理解と実装**
- **テーブルの紐付けの実装**
- **Modelにデータを挿入して取り出す**
---

## 🛠️ 使用技術
- **フレームワーク**: Django 5
- **データベース**: SQLite
- **開発環境**: Python 3.x, Django Shell
- **仮想環境**: venv

---

## 🚀 実行方法

### 1️⃣ **リポジトリをクローン**
```bash
git clone https://github.com/chaizhiyuan2501/ModelExam.git
cd ModelExam
```

### 2️⃣ **仮想環境の作成と有効化**
**Windows (PowerShell) の場合**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```
**Windows (\u30b3マンドプロンプト) の場合**
```cmd
venv\Scripts\activate.bat
```
**Mac / Linux の場合**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **必要なパッケージをインストール**
```bash
pip install django
```

### 4️⃣ **データベースをマイグレーション**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ **サーバーの起動**
```bash
python manage.py runserver
```

---

## 🎯 動作確認
```bash
python 01_insert_records.py
python 02_insert_records.py
```
main.pyとmain_02.pyを実行し､db.sqlite3ファイルの[students],[test_results],[classes]テーブルを確認してください

---
