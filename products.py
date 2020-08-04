import os
products = []

# 資料讀取
if os.path.isfile('products.csv'): #檔案檢查
    print('有哦！文件找到了！')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格'in line:
                continue
            name , price = line.strip().split(',')
            products.append([name, price])
else:
    print('Err，沒找到存檔文件…')
    us = input('輸入"y"建立新文件： ')
    if us == 'y':
        with open('products.csv', 'w', encoding = 'utf-8') as f:
            f.write('商品,價格\n')

# 使用者輸入商品名稱,價格
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break 
    price = input('請輸入價格： ')
    price = int(price)
    products.append([name, price])

# 印出所有商品
for a in products:
    print(a[0], '的價格為',a[1] )

# 資料存入.csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')