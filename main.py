import flet as ft
from information_page import InformationPage
from device_page import DevicePage

def main(page: ft.Page):
    page.title = "GT11 ELEC Form"
    page.scroll = "auto"
    page.window.width = 400
    page.window.height = 800
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20
    
    # ذخیره داده‌های برنامه
    page.session.set("form_data", {})
    
    # شروع با صفحه اطلاعات
    information_page = InformationPage(page)
    information_page.show()

ft.app(target=main)