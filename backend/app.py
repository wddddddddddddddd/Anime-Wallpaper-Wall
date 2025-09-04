from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 跨域允许
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 部署时改成前端域名更安全
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件夹
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/wallpapers")
def get_wallpapers():
    # base_url = "http://127.0.0.1:8000/static"  # 本地测试
    # 部署到服务器后改成服务器 IP 或域名，例如 http://yourdomain.com/static
    base_url = "/static"  # 部署到服务器后用公网 IP
    return [
        {
            "title": "Reading",
            "items": [
                {"url": f"{base_url}/1.webp", "title": "欢迎来到实力至上主义的教室", "color": "#b0b6a9"},
                {"url": f"{base_url}/2.webp", "title": "海贼王", "color": "#afa294"},
                {"url": f"{base_url}/3.webp", "title": "蓝色监狱", "color": "#3c3c3d"},
                {"url": f"{base_url}/4.webp", "title": "关于我转生变成史莱姆这档事", "color": "#b47460"},
                {"url": f"{base_url}/5.webp", "title": "辉夜大小姐想让我告白？～天才们的恋爱头脑战～", "color": "#60a6ce"},
                {"url": f"{base_url}/6.webp", "title": "异世界舅舅", "color": "#46666f"},
            ],
        },
        {
            "title": "Completed",
            "items": [
                {"url": f"{base_url}/7.webp", "title": "仙王的日常生活", "color": "#6e695e"},
                {"url": f"{base_url}/8.webp", "title": "一人之下", "color": "#b16e79"},
                {"url": f"{base_url}/9.webp", "title": "咒术回战", "color": "#bdbdbd"},
            ],
        },
        {
            "title": "Planning",
            "items": [
                {"url": f"{base_url}/10.webp", "title": "斗牌传说", "color": "#7b4d35"},
                {"url": f"{base_url}/11.webp", "title": "鬼灭之刃", "color": "#ceb5a8"},
                {"url": f"{base_url}/12.webp", "title": "全职猎人", "color": "#6d413f"},
                {"url": f"{base_url}/13.webp", "title": "宝可梦 钻石&珍珠", "color": "#666060"},
            ],
        },
    ]
