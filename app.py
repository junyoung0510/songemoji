import html

import streamlit as st

st.set_page_config(page_title="송이모지 이벤트", page_icon="💗", layout="centered")

# ───────────── 여기만 고치면 돼요 ─────────────
SERVER_NAME = "송이모지"
SERVER_INTRO = [
    "니트로 없이도 입장 가능한 고퀄 이모지 전문 서버입니다.",
    "디스보드·디코올 이모지 서버 후기 1등, 서버 내 후기 10000+로 증명된 퀄리티를 자랑합니다.",
    "소통이 매우 활발하며, 일반 서버원과 관리자 모두 먼저 친근하게 다가와 적응이 매우 쉽습니다.",
    "배너·이모지·하트·데코·서버프로필·서버배너까지 주문제작, 대량 주문, 외주 모두 가능한 믿고 맡기는 제작 서버입니다.",
]
# (아이콘, 큰 글씨, 작은 글씨) - 작은 글씨는 비워 둬도 돼요
FEATURES = [
    ("🎀", "5인 제작자 체계 운영 .ᐟ", "( 송이, 효정, 밍채, 다솜, 이슬 )"),
    ("💬", "소통이 매우 활발하며 애송이분들과 관리진 모두 먼저 친근하게 다가와 적응이 매우 쉬움 .ᐟ", ""),
    ("🏆", "디스보드·디코올 이모지 서버 후기 1등, 서버 내 후기 10000+로 증명된 퀄리티 자랑 .ᐟ", ""),
]
# 이미지 불러오는 방법
# 기본: 저장소의 static 폴더에서 불러와요 (.streamlit/config.toml 파일이 있어야 해요)
# 그래도 이미지가 안 보이면 깃허브 raw 주소를 적어 주세요. 예: "https://raw.githubusercontent.com/내아이디/저장소이름/main/static/"
IMAGE_BASE_URL = ""
HERO_IMAGE = "song-emoji.gif"  # 히어로(맨 위) 배경 이미지 - static 폴더 안의 파일 이름
LED_TEXT = "💗 송이모지에 오신 걸 환영해요! 편하게 놀다 가세요 💗"  # 상단 LED 간판에 흘러가는 환영 문구
# 시리즈 배너 구역: (아이콘, 구역 이름, [묶음들])
# 묶음 하나 = (배너 이미지 목록, 배너 소개 문구 목록) - 소개의 첫 줄은 크게, 나머지 줄은 작게 보여요
# 이미지는 static 폴더 안의 파일 경로(예: banners/a.gif)나 https 주소를 적어요. 묶음을 비워 두면 '준비 중'으로 보여요.
SERIES = [
    ("🧽", "스폰지밥", []),
    ("🌀", "우연운명필연", []),
    ("🏯", "사극", []),
    ("💑", "커플배너", []),
    ("💞", "커플이모지", []),
    ("🌸", "봄", []),
    ("🔞", "19금", []),
    ("💔", "이별", [
        (["banners/breakup-1.gif"], ["우리가 함께했던 추억은 기억해도 될까"]),
        (["banners/breakup-2.gif"], ["너와 함께한 모든 시간이 눈부셨다"]),
        (["banners/breakup-3.gif"], ["시간을 거스를 수 있다면 너를 만나러 가고싶어"]),
        (["banners/breakup-4.gif"], ["늦어도 좋으니, 마지막엔 내 곁에 돌아와줘"]),
        (["banners/breakup-5.gif"], ["비가 오는 날에는 네가 날 생각해주길"]),
        (["banners/breakup-6.gif"], ["상처 받아도 좋으니 다시 내 곁으로 와줘"]),
        (["banners/breakup-7.gif"], ["너를 사랑했기에 이제는 놔줘야 한다 널 위해서, 날 위해서"]),
        (["banners/breakup-8.gif"], ["너와 함께였던 그때로 돌아가고 싶어"]),
    ]),
    ("👥", "피플", [
        (
            ["banners/people-pink.gif", "banners/people-gray.gif", "banners/people-blue.gif"],
            ["거짓말은 최고의 사랑인걸!", "(무조건 진한색)"],
        ),
        (
            ["banners/love-candy.gif"],
            ["Love Candy"],
        ),
        (
            ["banners/your-name.gif"],
            ["Your name"],
        ),
        (
            ["banners/first-love.gif"],
            ["내 첫사랑이야!"],
        ),
        (
            ["banners/romantic-killer.gif"],
            ["로맨틱 킬러"],
        ),
        (
            ["banners/love-only-me.gif"],
            ["투명하게 나만 사랑해줘"],
        ),
        (
            ["banners/like-or-love.gif"],
            ["좋아하냐고? 아니 사랑해!"],
        ),
        (
            ["banners/falling-in-love.gif"],
            ["폴링인러브!"],
        ),
    ]),
]

# 구역별 색 테마: 이름을 적으면 그 구역만 다른 분위기로 바뀌어요 (현재: sad = 이별 컨셉의 어두운 회색 톤)
ZONE_THEMES = {}  # 이별 구역을 어두운 톤으로 쓰려면 {"이별": "sad"}로 바꿔요

# 구역 이름 옆에 보여 줄 안내 문구: 첫 줄은 크게, 나머지 줄은 작게 보여요
NOTICES = {
    "피플": [
        "모든 배너 가격은 3천원 입니다!",
        "* 무단 저장을 방지하기 위하여 저장 방지 글씨 넣었으며 받으시게 될 제작물에는 글씨 삭제할 예정입니다!",
        "* 8개 전부 구매 시 2천원 할인 된 가격인 30,000원에 구매하실 수 있습니다! !",
    ],
}
JOIN_URL = ""  # 디스코드 초대 링크를 넣으면 정보 바의 '참여 방법'이 링크로 바뀌어요 (예: https://discord.gg/xxxx)
EVENTS = [
    {"month": "12월", "day": "05", "title": "이벤트 이름 1", "desc": "이벤트 설명을 적어 주세요.", "status": "모집 중"},
    {"month": "12월", "day": "12", "title": "이벤트 이름 2", "desc": "이벤트 설명을 적어 주세요.", "status": "준비 중"},
    {"month": "12월", "day": "24", "title": "이벤트 이름 3", "desc": "이벤트 설명을 적어 주세요.", "status": "준비 중"},
]
# ───────────────────────────────────────────────


def clean(text):
    # 빈 줄과 들여쓰기를 없애서 마크다운이 HTML을 깨뜨리지 않게 해요.
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def img_url(value):
    # https 주소는 그대로, 파일 이름은 static 폴더(또는 IMAGE_BASE_URL) 기준 주소로 바꿔요.
    if value.startswith(("http://", "https://", "data:")):
        return value
    base = IMAGE_BASE_URL.rstrip("/") + "/" if IMAGE_BASE_URL else "app/static/"
    return base + value.lstrip("/")


hero_bg = '#f7a8c4 url("{}") center/cover no-repeat'.format(img_url(HERO_IMAGE))

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gowun+Dodum&family=DotGothic16&family=Chewy&display=swap');
.stApp{background-color:#fff3f7;background-image:radial-gradient(#f6c9d9 1.4px,transparent 1.4px);background-size:26px 26px}
[data-testid="stHeader"],#MainMenu,footer{display:none !important}
.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{overflow-x:hidden}
.block-container{max-width:1000px !important;padding:68px 16px 40px !important}
.sg,.sg *{font-family:"Gowun Dodum","Apple SD Gothic Neo","Malgun Gothic",sans-serif;box-sizing:border-box}
.sg h2,.sg h3,.sg .jua{font-family:"Jua","Apple SD Gothic Neo","Malgun Gothic",sans-serif;font-weight:400}
.sg a{text-decoration:none}
.sg-nav{position:fixed;top:0;left:0;right:0;z-index:999990;height:64px;display:flex;justify-content:space-between;align-items:center;
padding:0 max(16px,calc((100vw - 1000px) / 2));background:linear-gradient(180deg,#ffe0ec,#ffc4d8);
border-bottom:4px solid;border-image:linear-gradient(90deg,#9ccaff,#ffb6cf,#ffd166) 1}
.sg-brand{display:flex;align-items:center;gap:10px;color:#b0124f !important}
.sg-brand .mark{width:42px;height:42px;border-radius:50%;background:#ffd166;display:grid;place-items:center;font-size:1.4rem;box-shadow:0 0 0 3px rgba(255,209,102,.35)}
.sg-brand b{font-family:"Jua",sans-serif;font-weight:400;font-size:1.25rem;line-height:1.1;display:block}
.sg-brand small{font-family:"Chewy","Jua",sans-serif;font-size:.9rem;letter-spacing:.14em;color:#e8336f}
.sg-menu{display:flex;gap:4px;padding:5px;border-radius:999px;border:2px solid #fff;background:rgba(255,255,255,.6)}
.sg-menu a{color:#b0124f !important;padding:9px 20px;border-radius:999px;font-family:"Jua","Apple SD Gothic Neo","Malgun Gothic",sans-serif;font-size:1.15rem;white-space:nowrap}
.sg-menu a:hover,.sg-menu a[href="#home"]{background:#ffd166;color:#b0124f !important}
.sg:has(.sg-page:target) .sg-menu a[href="#home"]{background:transparent;color:#b0124f !important}
.sg:has(#events:target) .sg-menu a[href="#events"],.sg:has(#works:target) .sg-menu a[href="#works"],.sg:has(#songi:target) .sg-menu a[href="#works"],.sg:has(#series:target) .sg-menu a[href="#works"]{background:#ffd166;color:#b0124f !important}
.sg-page{display:none}
.sg-page:target{display:block}
.sg:has(.sg-page:target) .sg-home{display:none}
.sg-home,.sg-page:target{animation:pagein .35s ease-out}
@keyframes pagein{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.sg-home,.sg-page:target{animation:none}}
.sg-lights{position:fixed;top:68px;left:0;right:0;height:34px;z-index:999989;pointer-events:none;
background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='60' height='34'><path d='M0 4Q15 16 30 4T60 4' fill='none' stroke='%23ff8fb3' stroke-opacity='.9'/><path d='M15 11c-1-3-6-2-5 2 1 2 5 5 5 5s4-3 5-5c1-4-4-5-5-2z' fill='%23ffd166'/><path d='M45 11c-1-3-6-2-5 2 1 2 5 5 5 5s4-3 5-5c1-4-4-5-5-2z' fill='%23ff4d88'/></svg>") repeat-x}
.sg-hero{position:relative;width:100vw;margin-left:calc(50% - 50vw);height:clamp(480px,46vw,720px);overflow:hidden;background:__HERO_BG__;
display:flex;flex-direction:column;justify-content:space-between;padding:28px max(16px,calc((100vw - 1000px) / 2 + 16px))}
.sg-hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:45%;background:linear-gradient(transparent,rgba(176,18,79,.6));z-index:1}
.sg-hero > *{position:relative;z-index:2}
.sg-led{position:relative;align-self:flex-start;width:min(100%,340px);overflow:hidden;border-radius:14px;background:#2b0817;border:3px solid #fff;box-shadow:0 0 0 3px #b0124f,0 0 18px rgba(255,77,136,.75)}
.sg-led::after{content:"";position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(20,0,8,.7) 1px,transparent 1.5px);background-size:4px 4px}
.sg-led-track{display:flex;width:max-content;animation:ledmove 40s linear infinite}
.sg-led-track span{padding:0 36px;white-space:nowrap;line-height:44px;font-size:1.15rem;font-family:"DotGothic16","Gowun Dodum","Malgun Gothic",monospace;color:#ff9cc2;text-shadow:0 0 6px #ff4d88,0 0 14px #ff4d88}
@keyframes ledmove{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.sg-led-track{animation:none}}
.sg-cta{text-align:center}
.sg-cta p{margin:0 0 12px;color:#fff;font-weight:700;text-shadow:0 2px 8px rgba(120,0,50,.8)}
.sg-btn{display:inline-block;min-width:170px;margin:4px 6px;padding:13px 24px;border-radius:14px;font-family:"Jua",sans-serif;font-size:1.05rem;text-align:center}
.sg-btn.y{background:#ffd166;color:#b0124f !important;box-shadow:0 6px 0 #d9a52e}
.sg-btn.g{background:rgba(255,255,255,.18);color:#fff !important;border:2px solid #fff}
.fh{position:absolute !important;bottom:-30px;opacity:0;z-index:1 !important;animation:rise 7s linear infinite}
@keyframes rise{0%{transform:translateY(0);opacity:0}15%{opacity:.9}100%{transform:translateY(-480px);opacity:0}}
.sg-info{position:relative;z-index:3;margin:-44px 18px 0;display:grid;grid-template-columns:repeat(3,1fr);background:#fff;
border:2px solid #e8336f;border-radius:22px;box-shadow:0 8px 0 #f6c9d9;overflow:hidden}
.sg-info div{display:flex;align-items:center;gap:12px;padding:16px 20px;border-left:2px dashed #f6c9d9}
.sg-info div:first-child{border-left:0}
.sg-info .ic{width:46px;height:46px;border-radius:50%;display:grid;place-items:center;font-size:1.3rem;flex:none;background:linear-gradient(135deg,#9ccaff,#ffb6cf)}
.sg-info small{display:block;color:#8d5670;font-size:.78rem;line-height:1.3}
.sg-info b{font-family:"Jua",sans-serif;font-weight:400;color:#4d1630}
.sg-sec{padding-top:56px;scroll-margin-top:100px}
.sg-label{display:flex;align-items:center;gap:10px;font-size:.85rem;color:#4d1630}
.sg-label .dot{width:22px;height:22px;border-radius:50%;border:5px solid #b0124f;background:#fff}
.sg-label .tag{background:#b0124f;color:#ffd166;padding:2px 14px;border-radius:10px;letter-spacing:.05em}
.sg-label .dash{flex:0 0 100px;border-top:2px dashed #b0124f;opacity:.4}
.sg-sec h2{margin:10px 0 6px;font-size:2rem;color:#b0124f;line-height:1.25}
.sg-lead{margin:0 0 22px;color:#8d5670}
.sg-about{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.sg-card{border-radius:24px;padding:24px}
.sg-card.dark{background:#b0124f;color:#ffe8f0}
.sg-card.dark h3{color:#ffd166;font-size:1.35rem;margin:0 0 8px}
.sg-card.dark p{margin:0 0 12px;line-height:1.7}.sg-card.dark p:last-child{margin:0}
.sg-card.light{background:#fff;border:2px solid #f6c9d9;box-shadow:0 6px 0 #f6c9d9;color:#4d1630}
.sg-card.light div{display:flex;align-items:center;gap:12px;margin:10px 0}
.sg-card.light .ft{margin:0;font-family:"Jua","Apple SD Gothic Neo","Malgun Gothic",sans-serif;font-size:1.05rem;font-weight:400;line-height:1.5}
.sg-card.light .ft small{display:block;margin-top:2px;font-size:.8rem;font-weight:400;color:#8d5670}
.sg-card.light span{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:#ffe3ee;flex:none}
.sg-event{display:grid;grid-template-columns:100px 1fr;margin-bottom:14px;background:#fff;border:2px solid #f6c9d9;border-radius:22px;overflow:hidden;box-shadow:0 6px 0 #f6c9d9}
.sg-stub{background:#e8336f;color:#fff;text-align:center;padding:14px 6px;border-right:3px dashed #fff3f7;font-family:"Jua",sans-serif}
.sg-stub small{display:block;font-size:.85rem}
.sg-stub strong{font-weight:400;font-size:2.1rem;line-height:1.1}
.sg-ebody{padding:14px 20px}
.sg-ebody h3{margin:0;font-size:1.2rem;color:#4d1630}
.sg-ebody p{margin:2px 0 0;color:#8d5670;font-size:.95rem;line-height:1.5}
.sg-badge{margin-left:8px;padding:1px 12px;border-radius:999px;background:#ffd166;color:#b0124f;font-size:.78rem;vertical-align:middle}
.sg-back{display:inline-block;margin-bottom:6px;padding:6px 16px;border-radius:999px;background:#fff;border:2px solid #f6c9d9;color:#b0124f !important;font-family:"Jua",sans-serif}
.sg-works{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.sg-work{display:flex;align-items:center;gap:14px;padding:20px 22px;background:#fff;border:2px solid #f6c9d9;border-radius:24px;box-shadow:0 6px 0 #f6c9d9;color:#4d1630 !important;transition:transform .15s,border-color .15s}
.sg-work:hover{transform:translateY(-3px);border-color:#e8336f}
.sg-work .em{width:56px;height:56px;border-radius:50%;display:grid;place-items:center;font-size:1.8rem;background:#ffe3ee;flex:none}
.sg-work b{display:block;font-family:"Jua",sans-serif;font-weight:400;font-size:1.25rem;line-height:1.25}
.sg-work small{color:#8d5670}
.sg-work .go{margin-left:auto;color:#e8336f;font-size:1.6rem}
.sg-zone{margin-top:28px}
.sg-zonehead{display:flex;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:12px}
.sg-notice{flex:1 1 320px;padding:12px 18px;border-radius:18px;background:#fff7d6;border:2px dashed #ffc145;color:#4d1630}
.sg-notice b{display:block;font-family:"Jua",sans-serif;font-weight:400;font-size:1.1rem;color:#b0124f}
.sg-notice p{margin:3px 0 0;font-size:.88rem;line-height:1.5;color:#6d3a4f}
.sg-zone h3{display:inline-flex;align-items:center;gap:6px;margin:0;padding:6px 20px;border-radius:999px;background:#fff;border:2px solid #f6c9d9;box-shadow:0 4px 0 #f6c9d9;font-size:1.3rem;color:#b0124f}
.sg-banners{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.sg-banner{aspect-ratio:17/6;border-radius:20px;border:2px dashed #f6c9d9;background:#ffe3ee;display:grid;place-items:center;color:#8d5670;overflow:hidden;font-size:.9rem}
.sg-zone.sg-sad{margin-top:36px}
.sg-zone.sg-sad h3{background:#2b303b;border-color:#5a6275;box-shadow:0 4px 0 #0b0c10;color:#e3e9f6}
.sg-zone.sg-sad .sg-banner{background:#2b303b;border-color:#4a5163;color:#a9b2c6}
.sg-zone.sg-sad .sg-caption{background:#1c2029;border:2px solid #3f4655;border-left:8px solid #8e9bb5}
.sg-zone.sg-sad .sg-caption b{color:#e8eefc}
.sg-zone.sg-sad .sg-caption small{color:#a9b2c6}
.sg-zonebody{display:flex;flex-direction:column;gap:26px}
.sg-pair{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 16px}
.sg-pair .sg-banners{grid-template-columns:1fr}
@media (max-width:700px){.sg-pair,.sg-banners{grid-template-columns:1fr}}
.sg-caption{margin-top:12px;padding:12px 18px;border-radius:18px;background:#fff;border:2px solid #f6c9d9;border-left:8px solid #e8336f}
.sg-caption b{display:block;font-family:"Jua",sans-serif;font-weight:400;font-size:1.15rem;color:#b0124f}
.sg-caption small{display:block;color:#8d5670;font-size:.88rem}
.sg-banner:has(img){aspect-ratio:auto}
.sg-banner img{width:100%;height:100%;object-fit:cover;display:block}
.sg-empty{text-align:center;color:#8d5670;padding:20px}
.sg-foot{text-align:center;color:#8d5670;padding:44px 0 8px;font-size:.9rem}
@media (max-width:700px){
.sg-brand small{display:none}.sg-menu a{padding:8px 11px;font-size:.95rem}
.sg-info{grid-template-columns:1fr;margin:-30px 10px 0}
.sg-info div{border-left:0;border-top:2px dashed #f6c9d9}.sg-info div:first-child{border-top:0}
.sg-about{grid-template-columns:1fr}.sg-event{grid-template-columns:80px 1fr}.sg-hero{height:62vw;min-height:260px}}
</style>
""".replace("__HERO_BG__", hero_bg)

# 움직이는 하트 효과는 뺐어요.
floating = ""

if JOIN_URL:
    join_info = '<a href="{}" target="_blank" style="color:#b0124f">디스코드로 놀러 와요</a>'.format(html.escape(JOIN_URL))
else:
    join_info = "참여 링크 추가 예정"

led_group = "".join("<span>{}</span>".format(html.escape(LED_TEXT)) for _ in range(4))
led_html = '<div class="sg-led"><div class="sg-led-track">' + led_group + led_group + "</div></div>"

zones = []
for icon, name, groups in SERIES:
    blocks = []  # (배너가 1장인지, 묶음 HTML)
    for images, caption in groups:
        cells = "".join(
            '<div class="sg-banner"><img src="{}" alt="{}"></div>'.format(html.escape(img_url(u)), html.escape(name))
            for u in images
        )
        cap_html = ""
        if caption:
            cap_html = '<div class="sg-caption"><b>{}</b>{}</div>'.format(
                html.escape(caption[0]), "".join("<small>{}</small>".format(html.escape(line)) for line in caption[1:])
            )
        blocks.append((len(images) == 1, '<div class="sg-group"><div class="sg-banners">{}</div>{}</div>'.format(cells, cap_html)))

    # 배너가 1장인 묶음이 이어지면 가로로 3개씩 나란히 놓아요.
    parts, run = [], []
    for single, block in blocks + [(False, None)]:
        if single:
            run.append(block)
            continue
        if run:
            parts.append('<div class="sg-pair">{}</div>'.format("".join(run)))
            run = []
        if block is not None:
            parts.append(block)

    if not parts:
        cells = "".join('<div class="sg-banner">{} 배너 준비 중</div>'.format(html.escape(name)) for _ in range(2))
        parts.append('<div class="sg-group"><div class="sg-banners">{}</div></div>'.format(cells))
    note = NOTICES.get(name)
    note_html = ""
    if note:
        note_html = '<div class="sg-notice"><b>{}</b>{}</div>'.format(
            html.escape(note[0]), "".join("<p>{}</p>".format(html.escape(line)) for line in note[1:])
        )
    zones.append(
        '<div class="sg-zone{}"><div class="sg-zonehead"><h3>{} {}</h3>{}</div><div class="sg-zonebody">{}</div></div>'.format(
            " sg-" + ZONE_THEMES[name] if name in ZONE_THEMES else "", icon, html.escape(name), note_html, "".join(parts)
        )
    )
banners_html = "".join(zones)

intro_html = "".join("<p>{}</p>".format(html.escape(line)) for line in SERVER_INTRO)

features_html = "".join(
    '<div><span>{}</span><p class="ft">{}{}</p></div>'.format(
        html.escape(i), html.escape(t), "<small>{}</small>".format(html.escape(sub)) if sub else ""
    )
    for i, t, sub in FEATURES
)

if EVENTS:
    events_html = "".join(
        '<div class="sg-event"><div class="sg-stub"><small>{m}</small><strong>{d}</strong></div>'
        '<div class="sg-ebody"><h3>{t}<span class="sg-badge">{s}</span></h3><p>{x}</p></div></div>'.format(
            m=html.escape(e["month"]), d=html.escape(e["day"]), t=html.escape(e["title"]),
            s=html.escape(e["status"]), x=html.escape(e["desc"]),
        )
        for e in EVENTS
    )
else:
    events_html = '<div class="sg-empty">아직 예정된 이벤트가 없어요. 곧 알려 드릴게요!</div>'

BODY = """
<div class="sg">
<div class="sg-nav">
<a class="sg-brand" href="#home"><span class="mark">🍄</span><span><b>__NAME__</b><small>SONGEMOJI</small></span></a>
<div class="sg-menu"><a href="#home">홈</a><a href="#events">이벤트</a><a href="#works">작품</a></div>
</div>
<div class="sg-lights"></div>
<div class="sg-home" id="home">
<div class="sg-hero">
__FLOATING__
__LED__
</div>
<div class="sg-info">
<div><span class="ic">🍄</span><span><small>서버</small><b>__NAME__</b></span></div>
<div><span class="ic">🎟</span><span><small>진행 예정 이벤트</small><b>__COUNT__개</b></span></div>
<div><span class="ic">💬</span><span><small>참여 방법</small><b>__JOIN_INFO__</b></span></div>
</div>
<div class="sg-sec" id="about">
<div class="sg-label"><span class="dot"></span><span class="tag">LOVE NOTE 01</span><span>서버 소개</span><span class="dash"></span></div>
<h2>__NAME__는 이런 곳이에요</h2>
<p class="sg-lead">서버가 어떤 곳인지 한눈에 알아볼 수 있어요.</p>
<div class="sg-about">
<div class="sg-card dark"><h3>💗 서버 설명</h3><p>__INTRO__</p></div>
<div class="sg-card light">__FEATURES__</div>
</div>
</div>
</div>
<div class="sg-sec sg-page" id="events">
<div class="sg-label"><span class="dot"></span><span class="tag">LOVE NOTE 02</span><span>이벤트 목록</span><span class="dash"></span></div>
<h2>곧 열릴 이벤트예요</h2>
<p class="sg-lead">진행 예정인 이벤트를 날짜순으로 보여 줘요.</p>
__EVENTS__
</div>
<div class="sg-sec sg-page" id="works">
<div class="sg-label"><span class="dot"></span><span class="tag">WORKS</span><span>작품</span><span class="dash"></span></div>
<h2>작품</h2>
<p class="sg-lead">보고 싶은 작품을 골라 주세요.</p>
<div class="sg-works"><a class="sg-work" href="#songi"><span class="em">🍄</span><span><b>송이</b><small>눌러서 들어가기</small></span><span class="go">›</span></a></div>
</div>
<div class="sg-sec sg-page" id="songi">
<a class="sg-back" href="#works">← 작품으로</a>
<div class="sg-label"><span class="dot"></span><span class="tag">WORKS</span><span>송이</span><span class="dash"></span></div>
<h2>송이</h2>
<p class="sg-lead">송이의 작품을 구경해 보세요.</p>
<div class="sg-works"><a class="sg-work" href="#series"><span class="em">🎀</span><span><b>시리즈 배너 보러 가기</b><small>눌러서 들어가기</small></span><span class="go">›</span></a></div>
</div>
<div class="sg-sec sg-page" id="series">
<a class="sg-back" href="#songi">← 송이로</a>
<div class="sg-label"><span class="dot"></span><span class="tag">SERIES</span><span>시리즈 배너</span><span class="dash"></span></div>
<h2>시리즈 배너</h2>
<p class="sg-lead">송이의 시리즈 배너를 구역별로 모아 놓았어요.</p>
__BANNERS__
</div>
<div class="sg-foot">© __NAME__ · 사랑 가득 운영 중이에요 💗</div>
</div>
"""
for key, value in {
    "__NAME__": html.escape(SERVER_NAME),
    "__BANNERS__": banners_html,
    "__LED__": led_html,
    "__FLOATING__": floating,
    "__JOIN_INFO__": join_info,
    "__COUNT__": str(len(EVENTS)),
    "__INTRO__": intro_html,
    "__FEATURES__": features_html,
    "__EVENTS__": events_html,
}.items():
    BODY = BODY.replace(key, value)

st.markdown(clean(CSS) + "\n" + clean(BODY), unsafe_allow_html=True)
