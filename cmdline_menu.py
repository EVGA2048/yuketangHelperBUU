#+----+----+----+----+----+----+----+----+----+----+----+
#                     CMDLINE_MENU
# Developed by xxAp2005
# Last Update 2025/4/6Sun
# appreciate to MuWinds’s support
#
# current version v1.0.6
#
# 需要在项目requirements中添加的依赖有：
# colorama
#+----+----+----+----+----+----+----+----+----+----+----+

#import time

# 导入datetime模块
import datetime
# 导入os模块
import os
# 导入winsound库
import winsound
#导入颜色库
from colorama import Fore, Back, Style, init
init(autoreset=True)  # 自动重置颜色

#设置版本号
version = "1.0.6"

#设置状态信息颜色
INFO = Fore.LIGHTGREEN_EX + "INFO "
DEBUG = Fore.LIGHTYELLOW_EX + "DEBUG"
WARN = Fore.YELLOW + "WARN "
ERROR = Fore.RED + "ERROR"
FATAL = Fore.RED + "FATAL"
TIMER = Fore.LIGHTBLUE_EX + "TIMER"

enable_sound = True
enable_debug = "true"
if enable_debug == "true":
    print("[cmdline_menu]已启用debug输出")
    

#检测是否执行初始化
initialized = "false"

#获取系统用户名
username = os.getlogin()

#初始化头空格缺省全局变量
headerSpace = "    "

# 获取当前日期
current_date = datetime.date.today()

# 格式化日期
formatted_date = current_date.strftime("%Y-%m-%d")


#初始化菜单尺寸 边框样式
def initialize_menu_type(menu_type,border_style):
    global initialized
    global menuType,borderStyle
    # 检查 menu_type 是否合法
    if menu_type not in ["small", "medium", "large"]:
        echo_info(WARN,"无效的菜单类型. 选择 'small', 'medium', 或者 'large'.")
        echo_info(WARN,"cmdlineMENU初始化失败，菜单类型已缺省为small！")
        menuType = "small"
    
    # 检查 border_style 是否合法
    if border_style not in ["solid", "dashed"]:
        echo_info(WARN,"无效的边框样式. 选择 'solid' 或 'dashed'.")
        echo_info(WARN,"边框样式已缺省为 solid！")
        borderStyle = "solid"
    else:
        borderStyle = border_style

    if enable_debug == "true":
        echo_info("DEBUG","at def_initialize_menu_type menuType设置为" + menu_type)
    menuType = menu_type
    initialized = "true"
    if enable_debug == "true":
        echo_info("DEBUG","at def_initialize_menu_type initialized = " + initialized + " menuType=" + menuType)

    if enable_debug == "true":
        echo_info("DEBUG","cmdline_menu已启动，版本 " + version )

    # 调用 header_space 并传入 menuType
    header_space(menuType)  # 确保这里传入的是更新后的 menuType
    initialized = True
    if enable_debug == "true":
        echo_info("DEBUG", f"at def_initialize_menu_type menuType={menuType}, borderStyle={borderStyle}, initialized={initialized}")



def get_version():
    return version

def clear_cmdline_x10():                                    #生成10行空格用于清屏（保留历史消息）
    for _ in range(10):
        print(" ")

def clear_cmdline_x20():                                    #生成20行空格用于清屏（保留历史消息）
    for _ in range(20):
        print(" ")

def clear_cmdline_xN(N):                                    #生成N行空格用于清屏（保留历史消息）
    for _ in range(N):
        print(" ")

def full_clear():                                           #调用系统清屏（不保留历史消息）
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix/Linux
    else:
        os.system('clear')



def small_border(border_style):
    if border_style == "solid":
        print("+" + "-" * 30 + "+")
    elif border_style == "dashed":
        print("+----" * 7 + "+")

def medium_border(border_style):
    if border_style == "solid":
        print("+" + "-" * 50 + "+")
    elif border_style == "dashed":
        print("+----" * 12 + "+")

def large_border(border_style):
    if border_style == "solid":
        print("+" + "-" * 70 + "+")
    elif border_style == "dashed":
        print("+----" * 17 + "+")




#def small_border():
#   print("+" + "-" * 30 + "+")  # 总宽度 32 字符
#
#def medium_border():
#    print("+" + "-" * 50 + "+")  # 总宽度 52 字符
#
#def large_border():
#    print("+" + "-" * 70 + "+")  # 总宽度 72 字符


#def small_border():                                         #打印小尺寸边框
#    print("+-----+-----+-----+-----+-----+-----+")
#
#def medium_border():                                        #打印中尺寸边框
#    print("+-----+-----+-----+-----+-----+-----+-----+-----+")
#
#def large_border():                                         #打印大尺寸边框
#    print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")



def drawBorder(menuType , border_style):       
                                  #打印边框
    if menuType == "small":
        small_border(border_style)
    
    if menuType == "medium":
        medium_border(border_style)
    
    if menuType == "large":
        large_border(border_style)


def header_space(menuType):
    global headerSpace
    if enable_debug == "true":
        echo_info("DEBUG", "at def_header_space menuType = " + menuType)
        
    if menuType == "small":
        headerSpace = " " * 6  # 6个空格，适配 small_border 的宽度
    
    if menuType == "medium":
        headerSpace = " " * 10  # 10个空格，适配 medium_border 的宽度
    
    if menuType == "large":
        headerSpace = " " * 14  # 14个空格，适配 large_border 的宽度



#def header_space(menuType):
#    global headerSpace
#    if menuType == "small":
#        headerSpace = "    "
#    
#    if menuType == "medium":
#        headerSpace = "        "
#
#    if menuType == "large":
#        headerSpace = "            "
    


def create_option(sequence_number, option_text):
    global menuType
    # 统一格式：[序号] 选项文本，并自动适应 menuType 的缩进
    print(headerSpace + f"[{sequence_number}] {option_text}")

#def create_option(sequence_number, option_text):            #新建选项
#    global menuType
#    if menuType == "small":
#        print("    ")
#        print(headerSpace + "["+ sequence_number +"]" + option_text)
#
#    if menuType == "medium":
#        print("            ")
#        print(headerSpace + "            ["+ sequence_number +"]" + option_text)
#
#    if menuType == "large":
#        print("            ")
#        print(headerSpace + "            ["+ sequence_number +"]" + option_text)



def read_selection():                                       #读取选项
    selection = int(input("请输入选项序号："))
    return selection

def read_keyboardInput(title):                              #读取用户键盘输入
    content = str(input(title))
    return content


def singlespace():                                          #换行
    print(" ")



def muiltspace(amount):
    for _ in range(amount):
        print(" ")



def raw_text(text):                                         #打印文本
    print(headerSpace + text)



def welcome_panel(motd):
    singlespace()
    print(headerSpace + f"欢迎!  {username}     今天是 {formatted_date}")
    singlespace()
    raw_text(motd)


#def welcome_panel(motd):
#    singlespace()
#    print(headerSpace + "欢迎!  " + username + "     现在是 " + formatted_date)
#    singlespace()
#    raw_text(headerSpace + motd)

#打印带状态的信息
def echo_info(status,text):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    if (status == "INFO"):
        rawstatus = INFO
    if (status == "DEBUG"):
        rawstatus = DEBUG
    if (status == "WARN"):
        rawstatus = WARN
        warn_sound()
    if (status == "ERROR"):
        rawstatus = ERROR
        error_sound()
    if (status == "FATAL"):
        rawstatus = FATAL
        fatal_sound()
    if (status == "TIMER"):
        rawstatus = TIMER
        frequency = 2500  # 设置频率
        duration = 200  # 设置持续时间（毫秒）
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
    #else:
    #    rawstatus = status
    
    print("| " + formatted_time + " |" + " " + rawstatus + " " + Fore.RESET + "|" + " " + str(text))

def warn_sound():
    if enable_sound == True:
        frequency = 1200  # 设置频率
        duration = 200  # 设置持续时间（毫秒）
        winsound.Beep(frequency, duration)


def switch_sound():
    if enable_sound == True:
        frequency = 1200  # 设置频率
        duration = 200  # 设置持续时间（毫秒）
        winsound.Beep(frequency, duration)

def fatal_sound():
    if enable_sound == True:
        frequency = 1700  # 设置频率
        duration = 500  # 设置持续时间（毫秒）
        winsound.Beep(frequency, duration)

def error_sound():
    if enable_sound == True:
        frequency = 2000
        duration = 500
        winsound.Beep(frequency, duration)



def current_time():
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        raw_text(formatted_time)