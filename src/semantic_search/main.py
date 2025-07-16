from fastapi import FastAPI

from semantic_search.api.document import router as document_router
from semantic_search.environment.env_loader import load_env

# 環境変数の読み込み
load_env()

# FastAPIのインスタンスを作成
app = FastAPI(title="Semantic Search API", version="1.0.0")

# ルーターの登録
app.include_router(document_router)
