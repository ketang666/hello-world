import easygui as g
import random
times = 3
secret = random.randint(1,10)
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
while (guess != secret) and (times > 0):
    guess=g.integerbox('不妨猜一下','猜数字游戏',upperbound=9)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
        g.msgbox("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            g.msgbox("哥，大了大了~~~")
        else:
            g.msgbox("嘿，小了，小了~~~")
        if times > 0:
            g.msgbox("再试一次吧：")
        else:
            g.msgbox("机会用光咯T_T")
print("游戏结束，不玩啦^_^")
