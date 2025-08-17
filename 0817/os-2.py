import os

file = 'test/hello.txt'

# abspath 絕對路徑
print(os.path.abspath(file))

# basename 檔案名稱
print(os.path.basename(file))

# dirname 資料夾名稱
print(os.path.dirname(file))

# exists 判斷檔案是否存在
print(os.path.exists(file))
print(os.path.exists('test.txt'))

# split 將檔案路徑分割成dirname與basename並回傳tuple
print(os.path.split(file))

# splitext 將檔案路徑分割成路徑名稱與副檔名並回傳tuple
print(os.path.splitext(file))