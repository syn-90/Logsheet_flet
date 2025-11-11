
# import flet as ft
# from datetime import datetime

# class InformationPage:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.TEXT_COLOR = ft.Colors.WHITE
#         self.SKY_BLUE = ft.Colors.BLUE_400
        
#         self.shift_engineers_map = {
#             'A': ['A. Engineer1', 'A. Engineer2', 'A. Engineer3', 'A. Engineer4'],
#             'B': ['B. Engineer1', 'B. Engineer2', 'B. Engineer3', 'B. Engineer4'],
#             'C': ['C. Engineer1', 'C. Engineer2', 'C. Engineer3', 'C. Engineer4'],
#             'D': ['D. Engineer1', 'D. Engineer2', 'D. Engineer3', 'D. Engineer4']
#         }

#         self.create_controls()

#     def create_controls(self):
#         # ---------- DATE ----------
#         self.date_field = ft.TextField(
#             label="DATE *",
#             value=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
#             bgcolor=ft.Colors.WHITE10,
#             color=self.TEXT_COLOR,
#             border_color=self.SKY_BLUE,
#             text_size=16
#         )

#         # ---------- TIME ----------
#         self.time_group = ft.RadioGroup(
#             content=ft.ResponsiveRow(
#                 controls=[
#                     ft.Radio(value=t, label=t, label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                     for t in ['4:00', '8:00', '12:00', '16:00', '20:00', '0:00']
#                 ],
#                 columns=6,
#             )
#         )

#         # ---------- SHIFT ----------
#         self.shift_group = ft.RadioGroup(
#             content=ft.Row(
#                 [
#                     ft.Radio(value=s, label=s, label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                     for s in ['A', 'B', 'C', 'D']
#                 ],
#                 alignment=ft.MainAxisAlignment.SPACE_AROUND
#             )
#         )
#         self.shift_group.on_change = self.shift_changed

#         # ---------- LEADER ----------
#         self.leader_group = ft.RadioGroup(
#             content=ft.Column([
#                 ft.Radio(value=name, label=name, label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                 for name in ['A. ERFANIAN', 'A. MAHDI-ZADE', 'J. YARI', 'M. AHMADI']
#             ])
#         )

#         # ---------- ENGINEER ----------
#         self.eng_group = ft.RadioGroup(content=ft.Column([]))

#         # ---------- Buttons ----------
#         self.btn_cancel = ft.ElevatedButton(
#             "Cancel", on_click=self.on_cancel, bgcolor=ft.Colors.WHITE12, color=self.TEXT_COLOR
#         )
#         self.btn_next = ft.ElevatedButton(
#             "Next", on_click=self.on_next, bgcolor=self.SKY_BLUE, color=ft.Colors.WHITE
#         )

#     def show(self):
#         """نمایش صفحه اطلاعات"""
#         self.page.controls.clear()
        
#         btn_row = ft.Row([self.btn_cancel, self.btn_next], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

#         self.page.add(
#             ft.Text("📋 GT11 ELEC Form", size=25, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE),
#             self.date_field,
#             ft.Text("TIME *", color=self.SKY_BLUE, size=16),
#             self.time_group,
#             ft.Text("ATTENDING SHIFT *", color=self.SKY_BLUE, size=16),
#             self.shift_group,
#             ft.Text("SHIFT LEADER *", color=self.SKY_BLUE, size=16),
#             self.leader_group,
#             ft.Text("SHIFT ENGINEER *", color=self.SKY_BLUE, size=16),
#             self.eng_group,
#             ft.Divider(height=20, color=ft.Colors.WHITE24),
#             btn_row
#         )
#         self.page.update()

#     def shift_changed(self, e):
#         self.eng_group.content.controls.clear()
#         engineers = self.shift_engineers_map.get(self.shift_group.value, [])
#         for name in engineers:
#             self.eng_group.content.controls.append(
#                 ft.Radio(value=name, label=name, label_style=ft.TextStyle(color=self.TEXT_COLOR))
#             )
#         self.page.update()

#     def on_cancel(self, e):
#         self.date_field.value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#         self.time_group.value = None
#         self.shift_group.value = None
#         self.leader_group.value = None
#         self.eng_group.value = None
#         self.eng_group.content.controls.clear()
        
#         snack_bar = ft.SnackBar(ft.Text("Form reset"))
#         self.page.overlay.append(snack_bar)
#         snack_bar.open = True
#         self.page.update()

#     def on_next(self, e):
#         current_data = {
#             "date": self.date_field.value,
#             "time": self.time_group.value,
#             "shift": self.shift_group.value,
#             "shift_leader": self.leader_group.value,
#             "shift_engineer": self.eng_group.value,
#         }
        
#         missing = [k for k, v in current_data.items() if not v]
#         if missing:
#             snack_bar = ft.SnackBar(ft.Text(f"❗ Missing fields: {', '.join(missing)}"))
#             self.page.overlay.append(snack_bar)
#             snack_bar.open = True
#         else:
#             snack_bar = ft.SnackBar(ft.Text("✅ Form submitted successfully!"))
#             self.page.overlay.append(snack_bar)
#             snack_bar.open = True
#             print("Current form data:", current_data)
            
#             # ذخیره داده‌ها و انتقال به صفحه دستگاه
#             self.page.session.set("form_data", current_data)
#             self.go_to_device_page()
        
#         self.page.update()

#     def go_to_device_page(self):
#         """انتقال به صفحه دستگاه"""
#         from device_page import DevicePage
#         device_page = DevicePage(self.page)
#         device_page.show()

import flet as ft
from datetime import datetime

class InformationPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400

        # 📋 تعریف داده‌های مهندس‌ها بر اساس شیفت
        self.shift_engineers_map = {
            'A': ['A. Engineer1', 'A. Engineer2', 'A. Engineer3', 'A. Engineer4'],
            'B': ['B. Engineer1', 'B. Engineer2', 'B. Engineer3', 'B. Engineer4'],
            'C': ['C. Engineer1', 'C. Engineer2', 'C. Engineer3', 'C. Engineer4'],
            'D': ['D. Engineer1', 'D. Engineer2', 'D. Engineer3', 'D. Engineer4']
        }

        self.create_controls()
        self.page.on_resize = self.on_resize  # 📱 برای تغییر سایز واکنش‌گرا

    # ----------------------------------------------------------------
    def create_controls(self):
        # ---------- DATE ----------
        self.date_field = ft.TextField(
            label="DATE *",
            value=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            bgcolor=ft.Colors.WHITE10,
            color=self.TEXT_COLOR,
            border_color=self.SKY_BLUE,
            text_size=16,
            col={"xs": 12, "md": 6}  # در موبایل تمام عرض، در دسکتاپ نصف
        )

        # ---------- TIME ----------
        self.time_group = ft.RadioGroup(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Radio(value=t, label=t, label_style=ft.TextStyle(color=self.TEXT_COLOR))
                    for t in ['4:00', '8:00', '12:00', '16:00', '20:00', '0:00']
                ],
                columns=6,
            ),
        )

        # ---------- SHIFT ----------
        self.shift_group = ft.RadioGroup(
            content=ft.Row(
                [
                    ft.Radio(value=s, label=s, label_style=ft.TextStyle(color=self.TEXT_COLOR))
                    for s in ['A', 'B', 'C', 'D']
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        )
        self.shift_group.on_change = self.shift_changed

        # ---------- LEADER ----------
        self.leader_group = ft.RadioGroup(
            content=ft.Row(
                [
                    ft.Radio(value=name, label=name, label_style=ft.TextStyle(color=self.TEXT_COLOR))
                    for name in ['A. ERFANIAN', 'A. MAHDI-ZADE', 'J. YARI', 'M. AHMADI']
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        )

        # ---------- ENGINEER ----------
        self.eng_group = ft.RadioGroup(
            content=ft.Row([], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        )

        # ---------- Buttons ----------
        self.btn_cancel = ft.ElevatedButton(
            "Cancel", on_click=self.on_cancel, bgcolor=ft.Colors.WHITE12, color=self.TEXT_COLOR
        )
        self.btn_next = ft.ElevatedButton(
            "Next", on_click=self.on_next, bgcolor=self.SKY_BLUE, color=ft.Colors.WHITE
        )

    # ----------------------------------------------------------------
    def show(self):
        """📱 نمایش صفحه اطلاعات"""
        self.page.controls.clear()

        # 🔹 دکمه‌ها
        btn_row = ft.Row(
            [self.btn_cancel, self.btn_next],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            col={"xs": 12}
        )

        # 🔹 استفاده از ResponsiveRow برای کل صفحه
        layout = ft.ResponsiveRow(
            controls=[
                ft.Text("📋 GT11 ELEC Form", size=25, weight=ft.FontWeight.BOLD, color=self.SKY_BLUE, col={"xs": 12}),
                self.date_field,

                # دو ستونه: TIME و SHIFT کنار هم
                ft.Container(
                    content=ft.Column([
                        ft.Text("TIME *", color=self.SKY_BLUE, size=16),
                        self.time_group
                    ]),
                    col={"xs": 12, "md": 6}
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("ATTENDING SHIFT *", color=self.SKY_BLUE, size=16),
                        self.shift_group
                    ]),
                    col={"xs": 12, "md": 6}
                ),

                # دو ستونه: LEADER و ENGINEER کنار هم
                ft.Container(
                    content=ft.Column([
                        ft.Text("SHIFT LEADER *", color=self.SKY_BLUE, size=16),
                        self.leader_group
                    ]),
                    col={"xs": 12, "md": 6}
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("SHIFT ENGINEER *", color=self.SKY_BLUE, size=16),
                        self.eng_group
                    ]),
                    col={"xs": 12, "md": 6}
                ),

                ft.Divider(height=20, color=ft.Colors.WHITE24),

                btn_row
            ],
            spacing=10,
            run_spacing=10,
        )

        self.page.add(layout)
        self.page.update()

    # ----------------------------------------------------------------
    def shift_changed(self, e):
        """🔄 وقتی شیفت تغییر کنه، مهندس‌های مربوطه لود می‌شن"""
        self.eng_group.content.controls.clear()
        engineers = self.shift_engineers_map.get(self.shift_group.value, [])
        for name in engineers:
            self.eng_group.content.controls.append(
                ft.Radio(value=name, label=name, label_style=ft.TextStyle(color=self.TEXT_COLOR))
            )
        self.page.update()

    # ----------------------------------------------------------------
    def on_cancel(self, e):
        """🔄 بازگرداندن فرم به حالت اولیه"""
        self.date_field.value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.time_group.value = None
        self.shift_group.value = None
        self.leader_group.value = None
        self.eng_group.value = None
        self.eng_group.content.controls.clear()

        snack_bar = ft.SnackBar(ft.Text("Form reset"))
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()

    # ----------------------------------------------------------------
    def on_next(self, e):
        """✅ بررسی و ثبت اطلاعات فرم"""
        current_data = {
            "date": self.date_field.value,
            "time": self.time_group.value,
            "shift": self.shift_group.value,
            "shift_leader": self.leader_group.value,
            "shift_engineer": self.eng_group.value,
        }

        missing = [k for k, v in current_data.items() if not v]
        if missing:
            msg = f"❗ Missing fields: {', '.join(missing)}"
        else:
            msg = "✅ Form submitted successfully!"
            print("Current form data:", current_data)
            self.page.session.set("form_data", current_data)
            self.go_to_device_page()

        snack_bar = ft.SnackBar(ft.Text(msg))
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()

    # ----------------------------------------------------------------
    def on_resize(self, e):
        """📱 واکنش به تغییر اندازه صفحه"""
        width = self.page.window_width
        if width < 600:  # حالت موبایل
            self.page.padding = 10
        else:            # حالت لپ‌تاپ
            self.page.padding = 25
        self.page.update()

    # ----------------------------------------------------------------
    def go_to_device_page(self):
        """➡️ انتقال به صفحه بعدی (Device Page)"""
        from device_page import DevicePage
        device_page = DevicePage(self.page)
        device_page.show()
