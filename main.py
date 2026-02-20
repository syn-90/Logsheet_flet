import flet as ft
from information_page import InformationPage
from device_page import DevicePage
from device_section_page import DeviceSectionPage
from section_detail_page import SectionDetailPage


def main(page: ft.Page):
    page.title = "GT11 ELEC Form"
    page.scroll = "auto"
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20

    # init session if not present
    if page.session.get("form_data") is None:
        page.session.set("form_data", {})

    # ---------------------- ROUTING -------------------------
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        if page.route == "/" or page.route == "/information":
            page.views.append(InformationPage(page))

        elif page.route == "/device":
            page.views.append(DevicePage(page))

        elif page.route == "/sections":
            page.views.append(DeviceSectionPage(page))

        elif page.route == "/section_detail":
            page.views.append(SectionDetailPage(page))

        page.update()

    # ---------------------- BACK BUTTON ---------------------
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")   # <--- این خط باید آخر باشد!


ft.app(target=main, view=ft.AppView.FLET_APP)


