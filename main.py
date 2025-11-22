
import flet as ft

def main(page: ft.Page):
    page.title = "GT11 ELEC Form"
    page.scroll = "auto"
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20

    # init session if not present
    if page.session.get("form_data") is None:
        page.session.set("form_data", {})

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            from information_page import InformationPage
            page.views.append(InformationPage(page))
        elif page.route == "/device":
            from device_page import DevicePage
            page.views.append(DevicePage(page))
        elif page.route == "/sections":
            from device_section_page import DeviceSectionPage
            page.views.append(DeviceSectionPage(page))
        elif page.route == "/section_detail":  # اضافه کردن این روت (مشکل اصلی اینجا بود!)
            from section_detail_page import SectionDetailPage
            page.views.append(SectionDetailPage(page))
        else:
            # اگر روت نامعتبری بود، به اصلی برگرد
            page.views.append(ft.Text("Page not found! Returning to home..."))
            page.go("/")
        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

ft.app(target=main)

