from itertools  import dropwhile,takewhile,islice
from datetime import datetime
import time
from instaloader import Instaloader, InstaloaderContext
import instaloader
from openpyxl.styles import Font
from excel_control import download_file

# 记录开始时间
start_time = time.time()

# 初始化套件
L = instaloader.Instaloader()

# 使用 input() 接收用戶輸入
account = input("請輸入爬蟲用IG帳號: ")
password = input("請輸入爬蟲用IG密碼: ")
postid = input("想爬許的文章編號id (11碼) : ")

#登入ig帳號，部分操作會需要登入帳號，由於取得追蹤數貼文數不需要登入，這步驟省略
L.login(account, password)

#透過文章id"CGMTbf_lTIa" 取得post物件
post = instaloader.Post.from_shortcode(L.context, postid)

post_comments = post.get_comments()


# 創建陣列提取使用者帳號名
username=[]

# 創建陣列提取使用者留言
usernametext=[]

try:
    #迭代每則留言
    for comment in post_comments:
        username.append(comment.owner.username)
        usernametext.append(comment.text)

    if len(username) == len(usernametext):

        # 留言數和帳號數相同就下載成檔案
        download_file(username,usernametext)

    elif len(username) == 0:
        print("沒有留言")

    else:
        print("留言比帳號數多")
except Exception as e:
    print("發生錯誤：" + e)

# 记录结束时间
end_time = time.time()

# 计算时间间隔
elapsed_time = end_time - start_time

# 打印计时结果
print(f"操作执行时间：{elapsed_time:.2f} 秒")
done = input("另一鍵結束")






