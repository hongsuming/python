# 스레드를 이용해 날짜 및 시간 출력
import time

now = time.localtime()
print(now)
print(now.tm_year, ' ', now.tm_sec)

print('--------------')
import threading

def cal_show():
    now = time.localtime()
    print('현재는 {}년 {}월 {}일' .format(now.tm_year, now.tm_mon, now.tm_mday), end = ' ')
    print('{}시 {}분 {}초' .format(now.tm_hour, now.tm_min, now.tm_sec))
    
# cal_show()

def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_sec == 16:
            break
        cal_show()
        time.sleep(1)
        
th = threading.Thread(target=myRun)
th.start()

th.join()
print('프로그램 종료')
