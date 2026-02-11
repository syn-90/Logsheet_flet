
import flet as ft

class DevicePage(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page  # اول ست کن
        super().__init__(
            route="/device",
            controls=[],
            bgcolor=ft.Colors.BLACK,
            scroll=ft.ScrollMode.AUTO,
            padding=20
        )
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400

        self.DeviceList = [
            'ES & SCADA', 'ES & SCADA-TEMP', 'Battery-COM', 'MV BUS BCA BCB', 'BUB BUC',
            'Inverter 220vdc 220vac', 'LV BUS', 'LV EMERGANCY BUS BAR', 'BHT TRANS', 'DG',
            'FIN FAN SKID', 'OUTDOOR&INDOOR GAS SKID', 'Turbocompressor',
            'HYDR.SKID', 'LUBE OIL SKID', 'Gen.coolers', 'SLIP RING', 'AIR INTAKE',
            'Fuse box', 'BBE BUS BAR', 'DC UPS', 'CUN', 'BFE&BME',
            'Battery ', 'Transformers', 'Electical Fire container',
            'Diesel Pump Container', 'ROOM', 'CUN-P 01', 'Battery Room'
        ]

        # اینجا هیچ UI نساز! فقط متغیرها رو آماده کن

    def did_mount(self):
        # حالا self.page قطعاً مقدار داره و session در دسترسه
        self.build_ui()

    def build_ui(self):
        self.controls.clear()
        form_data = self.page.session.get("form_data") or {}  # حالا session وجود داره!

        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Form Information", size=18, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                    ft.Divider(height=6),
                    ft.Text(f"Date: {form_data.get('date','N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Time: {form_data.get('time','N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Shift: {form_data.get('shift','N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Leader: {form_data.get('shift_leader','N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Engineer: {form_data.get('shift_engineer','N/A')}", color=self.TEXT_COLOR),
                ], spacing=8),
                padding=15
            ),
            color=ft.Colors.WHITE12,
            margin=10
            
        )

        device_title = ft.Text("Choose Device", size=24, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE)

        buttons = [
            ft.ElevatedButton(
                text=device,
                width=320,
                height=50,
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
                on_click=lambda e, dev=device: self.on_select(dev)
            )
            for device in self.DeviceList
        ]

        grid = ft.ResponsiveRow(
            [ft.Container(content=btn, col={"xs": 12, "sm": 6, "md": 4}) for btn in buttons],
            run_spacing=12,
            spacing=12
        )

        back_btn = ft.ElevatedButton(
            "Back",
            on_click=lambda e: self.page.go("/"),
            bgcolor=ft.Colors.RED_400,
            color=ft.Colors.WHITE,
            width=150
        )

        self.controls = [
            info_card,
            ft.Divider(height=20),
            device_title,
            ft.Divider(height=10),
            grid,
            ft.Divider(height=40),
            ft.Container(content=back_btn, alignment=ft.alignment.center)
        ]

        # مهم: آپدیت صفحه بعد از تغییر controls
        self.page.update()

    def on_select(self, device_name):
        form_data = self.page.session.get("form_data") or {}
        form_data["device"] = device_name
        self.page.session.set("form_data", form_data)

        sb = ft.SnackBar(ft.Text(f"Device '{device_name}' selected!"))
        self.page.overlay.append(sb)
        sb.open = True

        self.page.go("/sections")
        self.page.update()  # حیاتی برای اندروید