from flask import Flask, render_template, request

app = Flask(__name__)

DESTINATIONS = [
    {
        "name": "阿里山國家風景區",
        "region": "嘉義・山林",
        "emoji": "🌲",
        "tag": "日出雲海・森林鐵路",
        "weather": "18°C・多雲偶晴",
        "feels": "體感 16°C",
        "wear": "薄羽絨／防風外套＋好走的防滑鞋",
        "stay": "建議停留 1–2 天",
        "hours": "森林遊樂區 24 小時開放",
        "food": ["奮起湖便當", "愛玉伯", "山葵料理"],
        "photo": "小火車從畫面左下切入，保留 2/3 森林與霧氣。",
        "transport": "嘉義高鐵／火車站轉台灣好行阿里山線；自駕約 2.5 小時。",
        "souvenir": "阿里山高山茶、山葵堅果、檜木香氛",
        "accent": "forest",
    },
    {
        "name": "九份老街",
        "region": "新北・山城",
        "emoji": "🏮",
        "tag": "山城夜景・紅燈籠",
        "weather": "23°C・有短暫雨",
        "feels": "體感 21°C",
        "wear": "輕防水外套、折傘；石階建議穿防滑鞋",
        "stay": "建議停留 3–5 小時",
        "hours": "多數店家 10:00–19:00",
        "food": ["芋圓", "草仔粿", "紅糟肉圓"],
        "photo": "傍晚藉由燈籠做前景，向下俯拍蜿蜒石階。",
        "transport": "瑞芳火車站轉 827、965 公車；台北可搭 1062。",
        "souvenir": "芋圓禮盒、九份茶包、手作燈籠",
        "accent": "lantern",
    },
    {
        "name": "日月潭",
        "region": "南投・湖畔",
        "emoji": "🛶",
        "tag": "環湖單車・湖光山色",
        "weather": "25°C・晴時多雲",
        "feels": "體感 26°C",
        "wear": "透氣短袖＋薄外套；騎車可帶防曬用品",
        "stay": "建議停留 1 天",
        "hours": "環湖步道全天；遊船約 09:00–17:00",
        "food": ["茶葉蛋", "邵族小米麻糬", "紅茶冰淇淋"],
        "photo": "在朝霧碼頭以船隻作前景，捕捉逆光下的湖面波光。",
        "transport": "台中高鐵／火車站轉南投客運；也適合租車環湖。",
        "souvenir": "魚池紅茶、香菇、邵族織品",
        "accent": "lake",
    },
]


@app.route("/")
def home():
    keyword = request.args.get("q", "").strip().lower()
    results = [d for d in DESTINATIONS if keyword in (d["name"] + d["region"] + d["tag"]).lower()] if keyword else DESTINATIONS
    return render_template("index.html", destinations=results, query=keyword)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
