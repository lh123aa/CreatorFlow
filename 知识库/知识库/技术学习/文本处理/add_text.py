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

# 尝试加载字体
def get_font(size):
    # 尝试系统字体
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Hiragino Sans GB W6.ttc",
        "C:/Windows/Fonts/msyhbd.ttc",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()

font = get_font(FONT_SIZE)

for idx, (name, text, bg_path) in enumerate(contents):
    # 打开背景图
    img = Image.open(bg_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # 计算文字位置（居中偏上）
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) // 2
    y = int(img.height * HEIGHT_POSITION) - text_height // 2
    
    # 绘制文字（深灰色，带点高级感）
    draw.text((x, y), text, font=font, fill="#333333")
    
    # 保存
    output_path = os.path.join(OUTPUT_DIR, f"{name}_{text}.jpg")
    img.save(output_path, "JPEG", quality=95)
    print(f"已生成: {output_path}")

print("\n全部完成！")
