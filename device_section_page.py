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
        """ذخیره تمام داده‌ها در Excel و بازگشت به صفحه اصلی"""
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
    
    # استفاده از ExcelHandler برای ذخیره در اکسل
        try:
            from excel_handler import ExcelHandler
            excel_handler = ExcelHandler()
            success = excel_handler.save_form_data(form_data)
        
            if success:
                self.show_success_and_return_to_main()
            else:
                self.show_error("❌ خطا در ذخیره داده‌ها در اکسل!")
            
        except ImportError as e:
            print(f"Error importing ExcelHandler: {e}")
            self.show_error(f"❌ خطا در بارگذاری ماژول Excel: {e}")
        except Exception as e:
            print(f"Error in Excel save: {e}")
            self.show_error(f"❌ خطا در ذخیره‌سازی: {str(e)}")

    def show_success_and_return_to_main(self):
        """نمایش پیام موفقیت و بازگشت به صفحه اصلی"""
        # پاک کردن صفحه و نمایش پیام موفقیت
        self.page.controls.clear()
        
        success_layout = ft.Column(
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, size=80, color=ft.Colors.GREEN),
                ft.Text("✅ موفقیت!", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                ft.Text("تمام داده‌ها با موفقیت در اکسل ذخیره شدند!", 
                    size=16, color=self.TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                ft.ProgressRing(width=30, height=30, color=ft.Colors.BLUE_400),
                ft.Text("در حال بازگشت به صفحه اصلی...", size=14, color=ft.Colors.GREY_400),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
        self.page.add(success_layout)
        self.page.update()
        
        # بازگشت به صفحه اصلی پس از تأخیر کوتاه
        import threading
        import time
        
        def navigate_to_main():
            time.sleep(2)  # تأخیر 2 ثانیه برای دیدن پیام موفقیت
            self.page.run_thread(self.go_to_main_page)
        
        thread = threading.Thread(target=navigate_to_main)
        thread.daemon = True
        thread.start()

    def go_to_main_page(self):
        """بازگشت به صفحه اصلی"""
        from information_page import InformationPage
        information_page = InformationPage(self.page)
        information_page.show()

    def show_error(self, message):
        """نمایش خطا"""
        snack_bar = ft.SnackBar(
            ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED_400
        )
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()

    def find_comment_field(self):
        """پیدا کردن فیلد کامنت"""
        # اگر فیلد کامنت در صفحه دارید، اینجا آن را پیدا کنید
        # مثال ساده:
        try:
            for control in self.page.controls:
                if hasattr(control, 'controls'):
                    for child in control.controls:
                        if isinstance(child, ft.TextField) and 'comment' in getattr(child, 'hint_text', '').lower():
                            return child
        except:
            pass
        return None