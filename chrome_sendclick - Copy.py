import win32gui, win32api,win32con
import time

namepg = "CPS Test / CPS Tester - Check Your CPS with Clicks Tracking Chart - Google Chrome"
hWnd = win32gui.FindWindow(None, namepg)
hWnd = win32gui.FindWindowEx(hWnd, None,None,None)

click = win32api.MAKELONG(985,400)


win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
time.sleep(1)
win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, click)




#website  https://www.arealme.com/click-speed-test/en/