import sys
from ChineseTimeNLP import TimeNormalizer, logger_format  # 引入包
from loguru import logger


logger.remove()
default_logger = logger.add(sys.stdout, format=logger_format, level="DEBUG")

tn = TimeNormalizer(isPreferFuture=False)

res = tn.parse(target=u"0.5小时后")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"2.5小时")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"3年后")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"10年后")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"下周五我有什么课")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"星期日我有什么课")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"八月十五号晚上我有什么课")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"晚上8点到上午10点之间")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(
    target=u"2013年二月二十八日下午四点三十分二十九秒", baseTime="2013-02-28 16:30:29"
)  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(
    target=u"我需要大概33天2分钟四秒", baseTime="2013-02-28 16:30:29"
)  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"今年儿童节晚上九点一刻")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"三日")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"7点4")  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print("====\n")

res = tn.parse(target=u"2个小时以前")
print(res)
print("====\n")

res = tn.parse(target=u"三日后")
print(res)
print("====\n")
res = tn.parse(target=u"三天后")
print(res)
print("====\n")
