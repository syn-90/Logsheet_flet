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

    try:
        # ---------------------- SESSION امن -------------------------
        # fallback برای نسخه‌های قدیمی Flet
        if hasattr(page, "session") and hasattr(page.session, "get"):
            if page.session.get("form_data") is None:
                page.session.set("form_data", {})
        else:
            # fallback: استفاده از دیکشنری محلی
            if not hasattr(page, "form_data"):
                page.form_data = {}

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

    except Exception as e:
        import traceback
        page.add(ft.Column([
            ft.Text("⚠️ خطا رخ داده است:", color=ft.Colors.RED, size=20),
            ft.Text(str(e), color=ft.Colors.RED),
            ft.Text(traceback.format_exc(), color=ft.Colors.RED, selectable=True)
        ]))
        page.update()

ft.app(target=main)