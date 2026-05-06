import json

# 1. 读取账单数据库
with open('./账单记录/账单数据库.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

bill_data = db['billData']

# 2. 读取HTML模板
with open('./账单记录/费用核算总表_2026-04-13.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 3. 生成新的billData数组字符串
new_bill_data_lines = []
for bill in bill_data:
    # 格式化每个账单项
    entry = f'''        {{
                "id": "{bill['id']}",
                "date": "{bill['date']}",
                "title": "{bill['title']}",
                "path": "{bill['path']}",
                "category": "{bill['category']}",
                "amount": {bill['amount']},
                "desc": "{bill['desc']}"'''
    # 如果有receipt_no字段，添加它
    if 'receipt_no' in bill:
        entry += f''',
                "receipt_no": "{bill['receipt_no']}"'''
    entry += '},'
    new_bill_data_lines.append(entry)

new_bill_data_str = '[\n' + '\n'.join(new_bill_data_lines) + '\n    ]'

# 4. 替换billData数组
import re
# 找到 const billData = [ 到 ] 的部分并替换
pattern = r'const billData = \[.*?\];'
replacement = f'const billData = {new_bill_data_str};'
new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# 5. 更新footer日期
new_html = new_html.replace('日期：2026-04-13', '日期：2026-04-15')

# 6. 保存新文件
output_path = './账单记录/费用核算总表_2026-04-15.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

# 7. 验证结果
with open(output_path, 'r', encoding='utf-8') as f:
    content = f.read()
    
# 统计账单数量
import re
bill_matches = re.findall(r'"id":\s*"([^"]+)"', content)
# 过滤掉非账单ID（如BS开头的银行小票ID）
bill_count = len([m for m in bill_matches if not m.startswith('BS')])
print(f"✅ 新HTML文件已生成: {output_path}")
print(f"📊 账单记录数量: {len(bill_data)} 条")
print(f"📅 更新日期: 2026-04-15")
print(f"📏 文件大小: {len(content)} 字节")
