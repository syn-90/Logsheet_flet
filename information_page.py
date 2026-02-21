# import flet as ft
# from datetime import datetime

# class InformationPage(ft.View):
#     def __init__(self, page: ft.Page):
#         self.page = page

#         # View استاندارد
#         super().__init__(
#             route="/",
#             controls=[],
#             padding=20,
#             bgcolor=ft.Colors.BLACK,
#             scroll=ft.ScrollMode.AUTO
#         )

#         self.TEXT_COLOR = ft.Colors.WHITE
#         self.SKY_BLUE = ft.Colors.BLUE_400

#         # لیست مهندس‌ها بر اساس شیفت
#         self.shift_engineers_map = {
#             'A': ['A. Engineer1', 'A. Engineer2', 'A. Engineer3', 'A. Engineer4'],
#             'B': ['B. Engineer1', 'B. Engineer2', 'B. Engineer3', 'B. Engineer4'],
#             'C': ['C. Engineer1', 'C. Engineer2', 'C. Engineer3', 'C. Engineer4'],
#             'D': ['D. Engineer1', 'D. Engineer2', 'D. Engineer3', 'D. Engineer4'],
#         }

#         self.build_ui()

#     # --------------------------------------------------------------

#     def build_ui(self):

#         # تاریخ
#         self.date_field = ft.TextField(
#             label="DATE *",
#             value=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
#             bgcolor=ft.Colors.WHITE10,
#             color=self.TEXT_COLOR,
#             border_color=self.SKY_BLUE,
#             text_size=16,
#             col={"xs": 12, "md": 6}
#         )

#         # زمان
#         self.time_group = ft.RadioGroup(
#             content=ft.ResponsiveRow(
#                 [
#                     ft.Radio(value=t, label=t,
#                              label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                     for t in ["4:00", "8:00", "12:00", "16:00", "20:00", "0:00"]
#                 ],
#                 columns=3
#             )
#         )

#         # شیفت
#         self.shift_group = ft.RadioGroup(
#             content=ft.Row(
#                 [
#                     ft.Radio(value=s, label=s,
#                              label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                     for s in ["A", "B", "C", "D"]
#                 ],
#                 alignment=ft.MainAxisAlignment.SPACE_AROUND
#             )
#         )
#         self.shift_group.on_change = self.shift_changed

#         # شیفت لیدر
#         self.leader_group = ft.RadioGroup(
#             content=ft.ResponsiveRow(
#                 [
#                     ft.Radio(value=name, label=name,
#                              label_style=ft.TextStyle(color=self.TEXT_COLOR))
#                     for name in ["A. ERFANIAN", "A. MAHDI-ZADE", "J. YARI", "M. AHMADI"]
#                 ],
#                 columns=2
#             )
#         )

#         # مهندس
#         self.eng_group = ft.RadioGroup(
#             content=ft.ResponsiveRow([], columns=2)
#         )

#         # دکمه next
#         self.btn_next = ft.ElevatedButton(
#             "Next",
#             on_click=self.on_next,
#             bgcolor=self.SKY_BLUE,
#             color=ft.Colors.WHITE,
#             width=200
#         )

#         # طراحی رسپانسیو صفحه
#         self.controls = [
#             ft.Text("📋 GT11 ELEC Form", size=25, weight="bold",
#                     color=self.SKY_BLUE, col={"xs": 12}),
#             self.date_field,

#             ft.Container(
#                 content=ft.Column([
#                     ft.Text("TIME *", color=self.SKY_BLUE),
#                     self.time_group
#                 ]),
#                 col={"xs": 12, "md": 6}
#             ),

#             ft.Container(
#                 content=ft.Column([
#                     ft.Text("ATTENDING SHIFT *", color=self.SKY_BLUE),
#                     self.shift_group
#                 ]),
#                 col={"xs": 12, "md": 6}
#             ),

#             ft.Container(
#                 content=ft.Column([
#                     ft.Text("SHIFT ENGINEER *", color=self.SKY_BLUE),
#                     self.leader_group
#                 ]),
#                 col={"xs": 12, "md": 6}
#             ),

#             ft.Container(
#                 content=ft.Column([
#                     ft.Text("SHIFT OPERATOR *", color=self.SKY_BLUE),
#                     self.eng_group
#                 ]),
#                 col={"xs": 12, "md": 6}
#             ),

#             ft.Container(
#                 content=self.btn_next,
#                 alignment=ft.alignment.center,
#                 col={"xs": 12}
#             )
#         ]

#     # --------------------------------------------------------------

#     def shift_changed(self, e):
#         """وقتی شیفت تغییر کند، مهندس‌های مرتبط لود می‌شوند"""
#         self.eng_group.content.controls.clear()
#         engineers = self.shift_engineers_map.get(self.shift_group.value, [])
#         for name in engineers:
#             self.eng_group.content.controls.append(
#                 ft.Radio(value=name, label=name,
#                          label_style=ft.TextStyle(color=self.TEXT_COLOR))
#             )
#         self.page.update()

#     # --------------------------------------------------------------

#     def on_next(self, e):
#             data = {
#             "date": self.date_field.value,
#             "time": self.time_group.value,
#             "shift": self.shift_group.value,
#             "shift_leader": self.leader_group.value,
#             "shift_engineer": self.eng_group.value,
#             }
#             missing = [k for k, v in data.items() if not v]
#             if missing:
#                 sb = ft.SnackBar(ft.Text(f"Missing fields: {', '.join(missing)}"))
#                 self.page.overlay.append(sb)
#                 sb.open = True
#                 self.page.update()  # این update برای SnackBar لازمه
#                 return

#             # ذخیره داده‌ها در session
#             self.page.session.set("form_data", data)

#             # تغییر مسیر + آپدیت صفحه (این خط حیاتی است!)
#             self.page.go("/device")
#             self.page.update()   # بدون این خط، روی اندروید کار نمی‌کنه!


import flet as ft
from datetime import datetime

class InformationPage(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page

        # View استاندارد
        super().__init__(
            route="/",
            controls=[],
            padding=20,
            bgcolor=ft.Colors.BLACK,
            scroll=ft.ScrollMode.AUTO
        )

        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400

        # لیست مهندس‌ها بر اساس شیفت
        self.shift_engineers_map = {
            'A': ['A. Engineer1', 'A. Engineer2', 'A. Engineer3', 'A. Engineer4'],
            'B': ['B. Engineer1', 'B. Engineer2', 'B. Engineer3', 'B. Engineer4'],
            'C': ['C. Engineer1', 'C. Engineer2', 'C. Engineer3', 'C. Engineer4'],
            'D': ['D. Engineer1', 'D. Engineer2', 'D. Engineer3', 'D. Engineer4'],
        }

        # تاریخ
        self.date_field = ft.TextField(
            label="DATE *",
            value=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            bgcolor=ft.Colors.WHITE10,
            color=self.TEXT_COLOR,
            border_color=self.SKY_BLUE,
            text_size=16,
        )

        # زمان - بدون مقدار پیش‌فرض
        time_radios = ft.Column([])
        for t in ["4:00", "8:00", "12:00", "16:00", "20:00", "0:00"]:
            time_radios.controls.append(
                ft.Radio(value=t, label=t,
                        label_style=ft.TextStyle(color=self.TEXT_COLOR))
            )
        self.time_group = ft.RadioGroup(
            content=time_radios,
            value=None  # بدون مقدار پیش‌فرض
        )

        # شیفت - بدون مقدار پیش‌فرض
        shift_radios = ft.Row(
            [
                ft.Radio(value=s, label=s,
                        label_style=ft.TextStyle(color=self.TEXT_COLOR))
                for s in ["A", "B", "C", "D"]
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
        self.shift_group = ft.RadioGroup(
            content=shift_radios,
            value=None,  # بدون مقدار پیش‌فرض
            on_change=self.shift_changed
        )

        # شیفت لیدر - بدون مقدار پیش‌فرض
        leader_radios = ft.Column([])
        for name in ["A. ERFANIAN", "A. MAHDI-ZADE", "J. YARI", "M. AHMADI"]:
            leader_radios.controls.append(
                ft.Radio(value=name, label=name,
                        label_style=ft.TextStyle(color=self.TEXT_COLOR))
            )
        self.leader_group = ft.RadioGroup(
            content=leader_radios,
            value=None  # بدون مقدار پیش‌فرض
        )

        # مهندس - خالی برای شروع
        self.eng_group = ft.RadioGroup(
            content=ft.Column([]),
            value=None  # بدون مقدار پیش‌فرض
        )

        # دکمه next
        self.btn_next = ft.ElevatedButton(
            "Next",
            on_click=self.on_next,
            bgcolor=self.SKY_BLUE,
            color=ft.Colors.WHITE,
            width=200
        )

        # طراحی ساده و رسپانسیو
        self.controls = [
            ft.Column(
                [
                    ft.Text("📋 GT11 ELEC Form",
                            size=25,
                            weight="bold",
                            color=self.SKY_BLUE),
                    
                    ft.Container(height=20),
                    
                    self.date_field,
                    
                    ft.Container(height=20),
                    
                    ft.Text("TIME *", color=self.SKY_BLUE, size=16),
                    self.time_group,
                    
                    ft.Container(height=20),
                    
                    ft.Text("ATTENDING SHIFT *", color=self.SKY_BLUE, size=16),
                    self.shift_group,
                    
                    ft.Container(height=20),
                    
                    ft.Text("SHIFT ENGINEER *", color=self.SKY_BLUE, size=16),
                    self.leader_group,
                    
                    ft.Container(height=20),
                    
                    ft.Text("SHIFT OPERATOR *", color=self.SKY_BLUE, size=16),
                    self.eng_group,
                    
                    ft.Container(height=30),
                    
                    ft.Row(
                        [self.btn_next],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True
            )
        ]

    # --------------------------------------------------------------

    def shift_changed(self, e):
        """وقتی شیفت تغییر کند، مهندس‌های مرتبط لود می‌شوند"""
        # پاک کردن محتوای قبلی
        self.eng_group.content.controls.clear()
        
        # اضافه کردن مهندس‌های جدید برای شیفت انتخاب شده
        engineers = self.shift_engineers_map.get(self.shift_group.value, [])
        for name in engineers:
            self.eng_group.content.controls.append(
                ft.Radio(value=name, label=name,
                        label_style=ft.TextStyle(color=self.TEXT_COLOR))
            )
        
        # مقدار انتخاب شده را به None برمی‌گردانیم تا هیچکدام انتخاب نباشند
        self.eng_group.value = None
        
        self.page.update()

    # --------------------------------------------------------------

    def on_next(self, e):
        data = {
            "date": self.date_field.value,
            "time": self.time_group.value,
            "shift": self.shift_group.value,
            "shift_leader": self.leader_group.value,
            "shift_engineer": self.eng_group.value,
        }
        
        missing = [k for k, v in data.items() if not v]
        if missing:
            # ایجاد SnackBar و اضافه کردن به صفحه
            snack_bar = ft.SnackBar(
                content=ft.Text(f"لطفاً فیلدهای زیر را پر کنید: {', '.join(missing)}"),
                bgcolor=ft.Colors.RED_400
            )
            self.page.overlay.append(snack_bar)
            snack_bar.open = True
            self.page.update()
            return

        # ذخیره داده‌ها در session
        self.page.session.set("form_data", data)

        # تغییر مسیر
        self.page.go("/device")



