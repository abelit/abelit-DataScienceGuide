import sys
import time

def process_bar():
    for i in range(1,101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "◼ "*(i//2), end="")
        sys.stdout.flush()
        time.sleep(0.05)


def testr():
    for i in range(22, 0, -1):
        print('\r%d' % i, end='') # end='' 默认为换行符\n ，修改为空不换行
        time.sleep(1) # 暂停1秒


def timebar():
    scale = 50
    print("start download".center(scale // 2 , "-"))
    start = time.perf_counter()

    for i in range(scale+1):
        a = "◼" * i
        b = "." * (scale-i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
        time.sleep(0.1)
    print("\n"+"download successfully".center(scale // 2,"-"))


def tpdmbar():
    from tqdm import tqdm

    for i in tqdm(range(1, 500)):
        time.sleep(0.01)
    time.sleep(0.5)

def progressbar():
    from progress.bar import IncrementalBar
    # mylist = [1,2,3,4,5,6,7,8]
    mylist = [i for  i in range(8)]

    bar = IncrementalBar('Countdown', max = len(mylist))

    for item in mylist:
        bar.next()
        time.sleep(1)
        bar.finish()

def aliveprogress():
    from alive_progress import alive_bar
    items = range(100)

    with alive_bar(len(items)) as bar:
        for item in items:
            bar()
            time.sleep(0.1)

def guibar():
    import PySimpleGUI as sg 
    mylist = [i for i in range(8)]
    for i, item in enumerate(mylist):
        sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist))
        time.sleep(1)
aliveprogress()