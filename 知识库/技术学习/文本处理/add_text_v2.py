from PIL import Image, ImageDraw, ImageFont
import os

# 参数配置
FONT_SIZE = 180
WIDTH_RATIO = 0.45
HEIGHT_POSITION = 0.45
OUTPUT_DIR = "imgs/260423_03_生图/测试103_高效阅读法/output"

# 文字内容
contents = [
    ("封面", "高效阅读法", "imgs/260423_04_生图/bg_0.jpg"),
    ("图1", "带着问题", "imgs/260423_04_生图/bg_1.jpg"),
    ("图2", "快速浏览", "imgs/260423_04_生图/bg_2.jpg"),
    ("图3", "笔记输出", "imgs/260423_04_生图/bg_3.jpg"),
    ("图4", "主题阅读", "imgs/260423_04_生图/bg_4.jpg"),
    ("图5", "定期复盘", "imgs/260423_04_生图/bg_5.jpg"),
    ("图6", "学以致用", "imgs/260423_04_生图/bg_6.jpg"),
]

# 使用内置默认字体（更大尺寸）
font = ImageFont.load_default(size=FONT_SIZE)

# 检查可用字体
import subprocess
result = subprocess.run(['fc-list', '--format=%{family}\n'], capture_output=True, text=True)
print("可用字体:", result.stdout[:500] if result.stdout else "无")

# 尝试使用Unicode字体
try:
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    ]
    for path in font_paths:
        if os.path.exists(path):
            print(f"找到字体: {path}")
            font = ImageFont.truetype(path, FONT_SIZE)
            break
except Exception as e:
    print(f"字体加载错误: {e}")

for idx, (name, text, bg_path) in enumerate(contents):
    img = Image.open(bg_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # 计算文字位置
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
    except:
        bbox = (0, 0, len(text)*FONT_SIZE*0.6, FONT_SIZE)
    
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) // 2
    y = int(img.height * HEIGHT_POSITION) - text_height // 2
    
    # 绘制文字（深灰色）
    draw.text((x, y), text, font=font, fill="#333333")
    
    output_path = os.path.join(OUTPUT_DIR, f"{name}_{text}.jpg")
    img.save(output_path, "JPEG", quality=95)
    print(f"已生成: {output_path} (文字位置: {x}, {y})")

print("\n全部完成！")
