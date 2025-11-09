import flet as ft
from device_sections_map import device_sections_map

class SectionDetailPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400
        self.current_field_index = 0
        self.fields_data = []
        self.section_data = {}

    def show(self):
        """نمایش صفحه جزئیات بخش با صفحه‌بندی"""
        self.page.controls.clear()
        
        # دریافت داده‌ها از session
        form_data = self.page.session.get("form_data") or {}
        self.device_name = form_data.get('device', 'Unknown Device')
        self.section_name = form_data.get('selected_section', 'Unknown Section')
        
        # اطلاعات بخش
        section_info = device_sections_map.get(self.device_name, {}).get(self.section_name, {})
        
        # آماده‌سازی لیست فیلدها
        self.prepare_fields_list(section_info)
        
        # نمایش اولین فیلد
        self.show_current_field()

    def prepare_fields_list(self, section_info):
        """آماده‌سازی لیست فیلدها"""
        self.fields_data = []
        
        # فیلدهای عددی
        numeric_fields = section_info.get('numeric_fields', {})
        for field_name, field_data in numeric_fields.items():
            self.fields_data.append({
                'type': 'numeric',
                'name': field_name,
                'unit': field_data.get('unit', ''),
                'range': field_data.get('range', None),
                'value': None
            })
        
        # فیلدهای گزینه‌ای
        option_fields = section_info.get('option_fields', {})
        for field_name, field_data in option_fields.items():
            self.fields_data.append({
                'type': 'option',
                'name': field_name,
                'options': field_data.get('options', []),
                'normal_option': field_data.get('normal', ''),
                'value': None
            })

    def show_current_field(self):
        """نمایش فیلد فعلی"""
        if self.current_field_index >= len(self.fields_data):
            self.save_all_data()
            return
        
        current_field = self.fields_data[self.current_field_index]
        
        # پاک کردن صفحه
        self.page.controls.clear()
        
        # ایجاد رابط کاربری برای فیلد فعلی
        self.create_field_ui(current_field)

    def create_field_ui(self, field):
        """ایجاد رابط کاربری برای فیلد فعلی"""
        # عنوان
        title = ft.Text(
            f"📊 {self.device_name} - {self.section_name}",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=self.SKY_BLUE
        )
        
        # پیشرفت
        progress_text = ft.Text(
            f"Field {self.current_field_index + 1} of {len(self.fields_data)}",
            size=14,
            color=ft.Colors.GREY_400
        )
        
        # نوار پیشرفت
        progress_bar = ft.ProgressBar(
            value=(self.current_field_index) / len(self.fields_data),
            width=400,
            color=self.SKY_BLUE
        )
        
        # فیلد اصلی
        field_control = self.create_field_control(field)
        
        # دکمه‌های ناوبری
        nav_buttons = self.create_navigation_buttons()
        
        # چیدمان اصلی
        main_layout = ft.Column(
            controls=[
                title,
                progress_text,
                progress_bar,
                ft.Divider(height=30),
                field_control,
                ft.Divider(height=30),
                nav_buttons
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.add(main_layout)
        self.page.update()

    def create_field_control(self, field):
        """ایجاد کنترل فیلد بر اساس نوع"""
        if field['type'] == 'numeric':
            return self.create_numeric_field_control(field)
        else:
            return self.create_option_field_control(field)

    def create_numeric_field_control(self, field):
        """ایجاد کنترل فیلد عددی"""
        field_name = field['name']
        unit = field['unit']
        value_range = field['range']
        
        # عنوان فیلد
        field_title = ft.Text(
            f"{field_name} ({unit})",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=self.TEXT_COLOR,
            text_align=ft.TextAlign.CENTER
        )
        
        # فیلد ورودی
        self.numeric_input = ft.TextField(
            label=f"Enter value in {unit}",
            keyboard_type=ft.KeyboardType.NUMBER,
            border_color=self.SKY_BLUE,
            bgcolor=ft.Colors.WHITE10,
            color=self.TEXT_COLOR,
            width=300,
            text_size=20,
            text_align=ft.TextAlign.CENTER,
            on_change=lambda e: self.validate_numeric_input(e, field)
        )
        
        # نمایش رنج نرمال
        range_info = ft.Text(
            f"Normal range: {value_range[0]} - {value_range[1]} {unit}" if value_range and len(value_range) == 2 else "No range specified",
            size=14,
            color=ft.Colors.GREY_400,
            text_align=ft.TextAlign.CENTER
        )
        
        # خطای اعتبارسنجی
        self.validation_error = ft.Text(
            "",
            size=16,
            color=ft.Colors.RED,
            text_align=ft.TextAlign.CENTER
        )
        
        return ft.Column([
            field_title,
            ft.Divider(height=20),
            self.numeric_input,
            ft.Divider(height=10),
            range_info,
            self.validation_error
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def create_option_field_control(self, field):
        """ایجاد کنترل فیلد گزینه‌ای"""
        field_name = field['name']
        options = field['options']
        normal_option = field['normal_option']
        
        # عنوان فیلد
        field_title = ft.Text(
            field_name,
            size=24,
            weight=ft.FontWeight.BOLD,
            color=self.TEXT_COLOR,
            text_align=ft.TextAlign.CENTER
        )
        
        # گروه رادیو
        self.radio_group = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(
                    value=opt,
                    label=opt,
                    label_style=ft.TextStyle(color=self.TEXT_COLOR, size=16)
                ) for opt in options
            ]),
            on_change=lambda e: self.validate_option_input(e, field)
        )
        
        # نمایش گزینه نرمال
        normal_info = ft.Text(
            f"Normal option: {normal_option}",
            size=14,
            color=ft.Colors.GREY_400,
            text_align=ft.TextAlign.CENTER
        )
        
        # هشدار
        self.option_warning = ft.Text(
            "",
            size=16,
            color=ft.Colors.ORANGE,
            text_align=ft.TextAlign.CENTER
        )
        
        return ft.Column([
            field_title,
            ft.Divider(height=20),
            self.radio_group,
            ft.Divider(height=10),
            normal_info,
            self.option_warning
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def create_navigation_buttons(self):
        """ایجاد دکمه‌های ناوبری"""
        is_last_field = self.current_field_index == len(self.fields_data) - 1
        is_first_field = self.current_field_index == 0
        
        # متن دکمه Previous بر اساس موقعیت
        previous_text = "Back to Sections" if is_first_field else "← Previous"
        
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    previous_text,
                    on_click=self.go_to_previous_field,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.RED_400,
                    )
                ),
                ft.ElevatedButton(
                    "Save" if is_last_field else "Next →",
                    on_click=self.save_and_continue,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.GREEN_400 if is_last_field else self.SKY_BLUE,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=400
        )

    def validate_numeric_input(self, e, field):
        """اعتبارسنجی فیلد عددی"""
        value = e.control.value
        
        if not value:
            self.validation_error.value = ""
            self.validation_error.update()
            return
        
        try:
            num_value = float(value)
            value_range = field['range']
            
            if value_range and len(value_range) == 2:
                min_val, max_val = value_range
                if num_value < min_val or num_value > max_val:
                    self.validation_error.value = f"⚠ Value outside normal range ({min_val} - {max_val})"
                    self.validation_error.color = ft.Colors.ORANGE
                else:
                    self.validation_error.value = "✅ Value within normal range"
                    self.validation_error.color = ft.Colors.GREEN
            else:
                self.validation_error.value = "✅ Value accepted"
                self.validation_error.color = ft.Colors.GREEN
                
        except ValueError:
            self.validation_error.value = "⚠ Please enter a valid number"
            self.validation_error.color = ft.Colors.RED
        
        self.validation_error.update()

    def validate_option_input(self, e, field):
        """اعتبارسنجی فیلد گزینه‌ای"""
        selected_value = e.control.value
        normal_option = field['normal_option']
        
        if selected_value:
            if selected_value != normal_option:
                self.option_warning.value = f"⚠ Warning: Normal option is '{normal_option}'"
                self.option_warning.color = ft.Colors.ORANGE
            else:
                self.option_warning.value = "✅ Normal option selected"
                self.option_warning.color = ft.Colors.GREEN
        else:
            self.option_warning.value = ""
        
        self.option_warning.update()

    def go_to_previous_field(self, e):
        """رفتن به فیلد قبلی یا بازگشت به بخش‌ها"""
        if self.current_field_index == 0:
            # اگر در اولین فیلد هستیم، به صفحه بخش‌ها برگرد
            self.go_back_to_sections()
        else:
            # برو به فیلد قبلی
            self.current_field_index -= 1
            self.show_current_field()

    def save_and_continue(self, e):
        """ذخیره فیلد فعلی و رفتن به بعدی"""
        current_field = self.fields_data[self.current_field_index]
        
        # دریافت و ذخیره مقدار فیلد فعلی
        if current_field['type'] == 'numeric':
            value = self.numeric_input.value
            if value:
                try:
                    current_field['value'] = float(value)
                except ValueError:
                    self.show_error("Please enter a valid number!")
                    return
            else:
                self.show_error("Please enter a value!")
                return
                
        else:  # option field
            value = self.radio_group.value
            if value:
                current_field['value'] = value
            else:
                self.show_error("Please select an option!")
                return
        
        # رفتن به فیلد بعدی یا ذخیره نهایی
        if self.current_field_index < len(self.fields_data) - 1:
            self.current_field_index += 1
            self.show_current_field()
        else:
            self.save_all_data()

    def save_all_data(self):
        """ذخیره تمام داده‌های بخش"""
        # جمع‌آوری تمام مقادیر
        section_data = {}
        for field in self.fields_data:
            if field['value'] is not None:
                section_data[field['name']] = field['value']
        
        # ذخیره در session
        form_data = self.page.session.get("form_data") or {}
        if 'sections' not in form_data:
            form_data['sections'] = {}
        
        form_data['sections'][self.section_name] = section_data
        self.page.session.set("form_data", form_data)
        
        # نمایش موفقیت و بازگشت سریع
        self.show_success_and_return()

    def show_success_and_return(self):
        """نمایش پیام موفقیت و بازگشت سریع به بخش‌ها"""
        # پاک کردن صفحه و نمایش پیام موفقیت
        self.page.controls.clear()
        
        success_layout = ft.Column(
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, size=80, color=ft.Colors.GREEN),
                ft.Text("✅ Success!", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                ft.Text(f"All data for {self.section_name} saved successfully!", 
                       size=16, color=self.TEXT_COLOR, text_align=ft.TextAlign.CENTER),
                ft.ProgressRing(width=30, height=30, color=ft.Colors.BLUE_400),
                ft.Text("Returning to sections page...", size=14, color=ft.Colors.GREY_400),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
        self.page.add(success_layout)
        self.page.update()
        
        # بازگشت سریع به صفحه بخش‌ها (بدون تأخیر قابل توجه)
        import threading
        import time
        
        def navigate_back():
            time.sleep(0.5)  # تأخیر بسیار کوتاه (نیم ثانیه)
            self.page.run_thread(self.go_back_to_sections)
        
        thread = threading.Thread(target=navigate_back)
        thread.daemon = True
        thread.start()

    def go_back_to_sections(self):
        """بازگشت به صفحه بخش‌ها"""
        from device_section_page import DeviceSectionPage
        section_page = DeviceSectionPage(self.page)
        section_page.show()

    def show_error(self, message):
        """نمایش خطا"""
        snack_bar = ft.SnackBar(
            ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED_400
        )
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()