"""src/teamtime.html(본문)을 어디서나 열 수 있는 index.html로 감싸는 빌드 스크립트."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
body = (root / "src" / "teamtime.html").read_text(encoding="utf-8")
head = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
(root / "index.html").write_text(head + body + "</body></html>", encoding="utf-8")
print("index.html 생성 완료")
