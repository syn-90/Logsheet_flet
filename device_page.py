
import flet as ft

class DevicePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400
        
        self.DeviceList = [
            'ES & SCADA', 'ES & SCADA-TEMP', 'Battery-COM', 'MV-COM', 'BUB BUC-COM', 'Inverter-COM', 'LV-COM',
            'LV EMERGANCY-COM', 'BHT TRANS', 'DG', 'FIN FAN SKID', 'OUTDOOR&INDOOR GAS SKID', 'Turbocompressor',
            'HYDR.SKID', 'LUBE OIL SKID', 'Gen.coolers', 'SLIP RING', 'AIR INTAKE', 'Fuse box', 'BBE BUS BAR',
            'DC UPS', 'GATE WAY', 'CUN', 'BFE&BME', 'Battery ', 'Transformers', 'Electical Fire container',
            'Diesel Pump Container', 'CONTAINAR', 'source'
        ]
        
        self.selected_device = None

    def show(self):
        """نمایش صفحه دستگاه"""
        self.page.controls.clear()
        
        # دریافت داده‌های فرم از session
        form_data = self.page.session.get("form_data") or {}
        
        # نمایش اطلاعات فرم
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("📋 Form Information", size=18, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                    ft.Divider(height=10),
                    ft.Text(f"Date: {form_data.get('date', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Time: {form_data.get('time', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Shift: {form_data.get('shift', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Leader: {form_data.get('shift_leader', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Engineer: {form_data.get('shift_engineer', 'N/A')}", size=14, color=self.TEXT_COLOR),
                ]),
                padding=15,
            ),
            color=ft.Colors.WHITE12
        )

        # عنوان صفحه دستگاه
        device_title = ft.Text("🏭 Choose Device", size=22, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE)
        
        # ایجاد دکمه‌های دستگاه
        device_buttons = []
        for device in self.DeviceList:
            btn = ft.ElevatedButton(
                text=device,
                on_click=lambda e, dev=device: self.select_device(dev),
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.BLUE_700,
                ),
                width=300,
                height=40
            )
            device_buttons.append(btn)

        # دکمه بازگشت
        back_btn = ft.ElevatedButton(
            "← Back to Form",
            on_click=self.go_back,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.RED_400,
            )
        )

        # چیدمان صفحه
        layout = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                info_card,
                ft.Divider(height=20),
                device_title,
                ft.Divider(height=10),
                *device_buttons,
                ft.Divider(height=30),
                back_btn
            ]
        )

        self.page.add(layout)
        self.page.update()

    def select_device(self, device_name):
        """انتخاب دستگاه و انتقال به صفحه بخش‌ها"""
        self.selected_device = device_name
        form_data = self.page.session.get("form_data") or {}
        form_data['device'] = device_name
        self.page.session.set("form_data", form_data)
        
        snack_bar = ft.SnackBar(ft.Text(f"✅ Device '{device_name}' selected!"))
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()
        
        print("Updated form data:", form_data)
        
        # انتقال خودکار به صفحه بخش‌های دستگاه
        self.go_to_device_sections()

    def go_to_device_sections(self):
        """انتقال به صفحه بخش‌های دستگاه"""
        from device_section_page import DeviceSectionPage
        section_page = DeviceSectionPage(self.page)
        section_page.show()
    def go_back(self, e):
        """بازگشت به صفحه فرم"""
        from information_page import InformationPage
        information_page = InformationPage(self.page)
        information_page.show()