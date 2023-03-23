import time
import win32gui, win32ui, win32con, win32api


def getin_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl,callback, hwnds)
    return hwnds



windowname = "*Untitled - Notepad"
hwnd = win32gui.FindWindow(None, windowname)
hwnd = getin_windows(hwnd)["Edit"]
win = win32ui.CreateWindowFromHandle(hwnd)

for x in range(10):
    win.SendMessage(win32con.WM_CHAR, ord("A"), 0)
    time.sleep(0.1)
