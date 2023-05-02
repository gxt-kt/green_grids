import datetime
import os
import random

# 设置起始日期和结束日期
start_date = datetime.date(2023, 5, 2)
end_date = datetime.date(2023, 9, 21)

commit_lists=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,3,8,10]

# 循环遍历日期范围
current_date = start_date
while current_date <= end_date:
    commit_date = datetime.datetime.combine(current_date, datetime.time(12, 0, 0))
    current_date += datetime.timedelta(days=1)

    random_val = random.randint(0, len(commit_lists)-1)
    for _ in range(0,commit_lists[random_val]):
        # print(commit_date)
        os.system("echo " + str(commit_date) + " >> add.txt")
        # 添加文件到暂存区
        os.system("git add .")

        # 设置提交日期和消息
        commit_message = "'commit on " + str(commit_date) + "'"
        os.system("git commit --date "+ commit_date.isoformat()+ " -m "+ commit_message)
        print("git commit --date " + commit_date.isoformat() + " -m " + commit_message)
        # subprocess.run(["git", "commit", "--date", commit_date.isoformat(), "-m", commit_message])

    # 前进到下一个日期
