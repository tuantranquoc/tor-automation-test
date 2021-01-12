import os
import time

def open_file():
    try:
        os.startfile('C:\Program Files\Cloudflare\Cloudflare WARP\Cloudflare WARP.exe')
    except:
        print('wrong file path')


def close_file():
    try:
        os.system('TASKKILL /F /IM notepad.exe')
    except:
        print(Exception)


if __name__ == "__main__":
    open_file()
    # time.sleep(2)
    # close_file()
