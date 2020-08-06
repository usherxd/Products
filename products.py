import os
products = []

# 資料讀取
def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格'in line:
                continue
            name , price = line.strip().split(',')
            products.append([name, price])
    return(products)


# 使用者輸入商品名稱,價格
def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if name == 'q':
            break 
        price = int(input('請輸入價格： '))
        products.append([name, price])
    return(products)


# 印出所有商品
def print_products(products):
    for a in products:
        print(a[0], '的價格為',a[1] )


# 資料存入.csv
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename): 
        products = read_file(filename)
    else: #沒找到檔案
        print('Err，沒找到存檔文件…')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()