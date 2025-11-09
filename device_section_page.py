import flet as ft
from device_sections_map import device_sections_map  # import دیکشنری بخش‌ها
from excel_handler import ExcelHandler
class DeviceSectionPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400
        self.selected_section = None
        self.section_buttons = []

    def show(self):
        """نمایش صفحه بخش‌های دستگاه"""
        self.page.controls.clear()
        
        # دریافت داده‌های فرم از session
        form_data = self.page.session.get("form_data") or {}
        device_name = form_data.get('device', 'Unknown Device')
        
        # عنوان صفحه
        title = ft.Text(
            f"🏭 {device_name} - Sections", 
            size=22, 
            weight=ft.FontWeight.BOLD, 
            color=self.SKY_BLUE
        )
        
        # نمایش اطلاعات دستگاه
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("📋 Device Information", size=18, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                    ft.Divider(height=10),
                    ft.Text(f"Device: {device_name}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Date: {form_data.get('date', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Time: {form_data.get('time', 'N/A')}", size=14, color=self.TEXT_COLOR),
                    ft.Text(f"Shift: {form_data.get('shift', 'N/A')}", size=14, color=self.TEXT_COLOR),
                ]),
                padding=15,
            ),
            color=ft.Colors.WHITE12
        )

        # بخش‌های دستگاه
        sections_container = self.create_sections_container(device_name)
        
        # فیلد کامنت
        comment_section = self.create_comment_section()
        
        # دکمه‌های ناوبری
        buttons_row = self.create_buttons_row()

        # چیدمان اصلی
        layout = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                title,
                ft.Divider(height=20),
                info_card,
                ft.Divider(height=20),
                ft.Text("📂 Select Section", size=18, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                sections_container,
                ft.Divider(height=20),
                comment_section,
                ft.Divider(height=30),
                buttons_row
            ]
        )

        self.page.add(layout)
        self.page.update()

    def create_sections_container(self, device_name):
        """ایجاد کانتینر بخش‌های دستگاه"""
        sections_dict = device_sections_map.get(device_name, {})
        
        if not sections_dict:
            return ft.Container(
                content=ft.Text("No sections available for this device", color=ft.Colors.ORANGE),
                padding=10
            )
        
        section_controls = []
        self.section_buttons = []
        
        for section_name in sections_dict.keys():
            btn = self.create_section_button(section_name)
            self.section_buttons.append(btn)
            section_controls.append(btn)
        
        return ft.Column(controls=section_controls, spacing=10)

    def create_section_button(self, section_name):
        """ایجاد دکمه بخش"""
        return ft.ElevatedButton(
            text=section_name,
            on_click=lambda e, sec=section_name: self.select_section(sec),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_700,
            ),
            width=350,
            height=45
        )

    def create_comment_section(self):
        """ایجاد بخش کامنت"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("💬 Additional Comments", size=16, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
                    ft.Divider(height=10),
                    ft.TextField(
                        hint_text="Enter any additional comments or notes...",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                        border_color=self.SKY_BLUE,
                        bgcolor=ft.Colors.WHITE10,
                        color=self.TEXT_COLOR
                    )
                ]),
                padding=15,
            ),
            color=ft.Colors.WHITE12
        )

    def create_buttons_row(self):
        """ایجاد ردیف دکمه‌ها"""
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    "← Back to Devices",
                    on_click=self.go_back,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.RED_400,
                    )
                ),
                ft.ElevatedButton(
                    "Save All Data",
                    on_click=self.save_all_data,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.GREEN_400,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    def select_section(self, section_name):
        """انتخاب بخش دستگاه"""
        self.selected_section = section_name
        
        # برجسته کردن دکمه انتخاب شده
        for btn in self.section_buttons:
            if btn.text == section_name:
                btn.bgcolor = ft.Colors.GREEN_400
            else:
                btn.bgcolor = ft.Colors.BLUE_700
            btn.update()
        
        # ذخیره بخش انتخاب شده
        form_data = self.page.session.get("form_data") or {}
        if 'sections' not in form_data:
            form_data['sections'] = {}
        
        form_data['selected_section'] = section_name
        
        if section_name not in form_data['sections']:
            form_data['sections'][section_name] = {}
        
        self.page.session.set("form_data", form_data)
        
        # نمایش پیام
        snack_bar = ft.SnackBar(ft.Text(f"✅ Section '{section_name}' selected!"))
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        
        print("Selected section:", section_name)
        print("Current form data:", form_data)
        
        # انتقال به صفحه جزئیات بخش
        self.go_to_section_details()

    def go_to_section_details(self):
        """انتقال به صفحه جزئیات بخش"""
        from section_detail_page import SectionDetailPage
        detail_page = SectionDetailPage(self.page)
        detail_page.show()

    def go_back(self, e):
        """بازگشت به صفحه دستگاه"""
        from device_page import DevicePage
        device_page = DevicePage(self.page)
        device_page.show()

    def save_all_data(self, e):
        """ذخیره تمام داده‌ها"""
        form_data = self.page.session.get("form_data") or {}
        
        # ذخیره کامنت
        comment_field = self.find_comment_field()
        if comment_field:
            form_data['comment'] = comment_field.value
        
        # فرمت زمان
        if 'time' in form_data:
            time_str = form_data['time']
            if ":" in time_str:
                form_data['time'] = time_str.split(":")[0]
            print(f"🕒 Final time: {form_data['time']}")
        
        # ذخیره در session
        self.page.session.set("form_data", form_data)
        
        # اینجا می‌توانید داده‌ها را به Excel ذخیره کنید
        success = self.save_to_excel(form_data)
        
        if success:
            snack_bar = ft.SnackBar(ft.Text("✅ All data saved successfully!"))
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            
            # بازگشت به صفحه اصلی
            from information_page import InformationPage
            information_page = InformationPage(self.page)
            information_page.show()
        else:
            snack_bar = ft.SnackBar(ft.Text("❌ Error saving data!"))
            self.page.overlay.append(snack_bar)
            snack_bar.open = True

    def find_comment_field(self):
        """پیدا کردن فیلد کامنت در کنترل‌های صفحه"""
        for control in self.page.controls[0].controls:  # فرض می‌کنیم layout اصلی Column است
            if hasattr(control, 'content') and hasattr(control.content, 'controls'):
                for sub_control in control.content.controls:
                    if isinstance(sub_control, ft.TextField) and sub_control.hint_text == "Enter any additional comments or notes...":
                        return sub_control
        return None

    def save_to_excel(self, form_data):
        """ذخیره داده‌ها در Excel"""
        try:
            # اینجا کد ذخیره در Excel را قرار دهید
            print("📊 Saving to Excel:", form_data)
            return True
        except Exception as e:
            print("❌ Error saving to Excel:", e)
            return False