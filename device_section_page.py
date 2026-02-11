

import flet as ft
from device_sections_map import device_sections_map
from excel_handler import ExcelHandler


class DeviceSectionPage(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__(
            route="/sections",
            controls=[],
            bgcolor=ft.Colors.BLACK,
            scroll=ft.ScrollMode.AUTO,
            padding=20
        )
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400
        self.section_buttons = []  # برای برجسته کردن دکمه انتخاب‌شده (اختیاری)

        # هیچ UI نساز! فقط متغیرها رو آماده کن
    def did_mount(self):
        self.page.update()  # حیاتی

        form_data = self.page.session.get("form_data") or {}
        device_name = form_data.get('device', 'Unknown')

        if not device_name or device_name == 'Unknown':
            self.page.go("/device")
            self.page.update()
            return

        # فقط یک بار UI رو بساز — این خط مشکل صفحه سیاه رو ۱۰۰٪ حل میکنه!
        if not hasattr(self, '_ui_built') or not self._ui_built:
            self.build_ui()
            self._ui_built = True

    def build_ui(self):
        self.controls.clear()
        form_data = self.page.session.get("form_data") or {}
        device_name = form_data.get('device', 'Unknown Device')

        # عنوان اصلی
        title = ft.Text(
            f"{device_name} - Sections",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=self.SKY_BLUE
        )

        # کارت اطلاعات دستگاه
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Device Information", size=18, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                    ft.Divider(height=8),
                    ft.Text(f"Device: {device_name}", color=self.TEXT_COLOR),
                    ft.Text(f"Date: {form_data.get('date', 'N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Time: {form_data.get('time', 'N/A')}", color=self.TEXT_COLOR),
                    ft.Text(f"Shift: {form_data.get('shift', 'N/A')}", color=self.TEXT_COLOR),
                ], spacing=6),
                padding=15
            ),
            color=ft.Colors.WHITE12,
            margin=10
        )

        # بخش‌های دستگاه
        sections = device_sections_map.get(device_name, {})
        if not sections:
            sections_container = ft.Container(
                content=ft.Text("No sections available for this device", color=ft.Colors.ORANGE_700, size=18),
                padding=20,
                alignment=ft.alignment.center
            )
        else:
            self.section_buttons = []
            buttons = []
            for section_name in sections.keys():
                btn = ft.ElevatedButton(
                    text=section_name,
                    width=360,
                    height=50,
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        elevation=4
                    ),
                    on_click=lambda e, sec=section_name: self.select_section(sec)
                )
                self.section_buttons.append(btn)
                buttons.append(btn)

            sections_container = ft.ResponsiveRow(
                [ft.Container(content=btn, col={"xs": 12, "md": 6, "lg": 4}) for btn in buttons],
                run_spacing=12,
                spacing=12
            )

        # فیلد کامنت
        self.comment_field = ft.TextField(
            hint_text="Enter any additional comments or observations...",
            multiline=True,
            min_lines=3,
            max_lines=6,
            border_color=self.SKY_BLUE,
            bgcolor=ft.Colors.WHITE10,
            color=self.TEXT_COLOR,
            text_size=16,
            width=500
        )
        # # بازگردانی کامنت قبلی اگر وجود داشته باشه
        # saved_comment = form_data.get('comment')
        # if saved_comment:
        #     self.comment_field.value = saved_comment

        # دکمه‌ها
        btn_back = ft.ElevatedButton(
            "Back to Devices",
            on_click=lambda e: self.page.go("/device"),
            bgcolor=ft.Colors.RED_400,
            color=ft.Colors.WHITE,
            width=180,
            height=50
        )

        btn_save_all = ft.ElevatedButton(
            "Save All Data → Excel",
            on_click=lambda e: self.save_all_data(),
            bgcolor=ft.Colors.GREEN_500,
            color=ft.Colors.WHITE,
            width=250,
            height=50,
            icon=ft.Icons.SAVE
        )

        # چیدمان نهایی
        self.controls = [
            title,
            ft.Divider(height=15),
            info_card,
            ft.Divider(height=20),
            ft.Text("Select Section", size=20, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
            ft.Divider(height=10),
            sections_container,
            ft.Divider(height=20),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Additional Comments", color=self.SKY_BLUE, size=16, weight=ft.FontWeight.BOLD),
                        self.comment_field
                    ], spacing=8),
                    padding=15
                ),
                color=ft.Colors.WHITE12,
                margin=10
            ),
            ft.Divider(height=20),
            ft.Row(
                [btn_back, btn_save_all],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Divider(height=30)
        ]

        # آپدیت صفحه
        self.page.update()

    def select_section(self, section_name):
        form_data = self.page.session.get("form_data") or {}
        form_data['selected_section'] = section_name
        self.page.session.set("form_data", form_data)

        # برجسته کردن دکمه انتخاب‌شده (اختیاری)
        for btn in self.section_buttons:
            if btn.text == section_name:
                btn.bgcolor = ft.Colors.GREEN_600
            else:
                btn.bgcolor = ft.Colors.BLUE_700
            btn.update()

        sb = ft.SnackBar(ft.Text(f"Section '{section_name}' selected!"))
        self.page.overlay.append(sb)
        sb.open = True

        self.page.go("/section_detail")
        self.page.update()  # حیاتی برای اندروید

    def save_all_data(self):
        # ذخیره کامنت
        form_data = self.page.session.get("form_data") or {}
        if self.comment_field.value:
            form_data['comment'] = self.comment_field.value.strip()
        self.page.session.set("form_data", form_data)

        try:
            excel = ExcelHandler()
            success = excel.save_form_data(form_data)
            if success:
                sb = ft.SnackBar(
                    ft.Text("All data saved successfully to Excel!"),
                    bgcolor=ft.Colors.GREEN
                )
                self.page.overlay.append(sb)
                sb.open = True
                self.page.update()

                # برگشت به صفحه دستگاه‌ها
                self.page.go("/device")
                self.page.update()
            else:
                self.show_error("Failed to save data. Check console.")
        except Exception as e:
            self.show_error(f"Error saving to Excel: {str(e)}")

    def show_error(self, msg):
        sb = ft.SnackBar(ft.Text(msg), bgcolor=ft.Colors.RED_600)
        self.page.overlay.append(sb)
        sb.open = True
        self.page.update()