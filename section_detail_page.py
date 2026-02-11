

import flet as ft
from device_sections_map import device_sections_map


class SectionDetailPage(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__(
            route="/section_detail",
            controls=[],
            bgcolor=ft.Colors.BLACK,
            scroll=ft.ScrollMode.AUTO,
            padding=20
        )
        self.TEXT_COLOR = ft.Colors.WHITE
        self.SKY_BLUE = ft.Colors.BLUE_400
        self.current_field_index = 0
        self.fields_data = []
        self.section_name = None
        self.device_name = None

    # def did_mount(self):
    #     form_data = self.page.session.get("form_data") or {}
    #     self.device_name = form_data.get('device', 'Unknown Device')
    #     self.section_name = form_data.get('selected_section', 'Unknown Section')

    #     section_info = device_sections_map.get(self.device_name, {}).get(self.section_name, {})
    #     if not section_info:
    #         self.show_error("Section data not found!")
    #         return

    #     self.prepare_fields_list(section_info)
    #     self.show_current_field()پ
    def did_mount(self):
            self.page.update()

            form_data = self.page.session.get("form_data") or {}
            self.device_name = form_data.get('device', 'Unknown')
            self.section_name = form_data.get('selected_section')

            if not self.section_name:
                self.page.go("/sections")
                self.page.update()
                return

            section_info = device_sections_map.get(self.device_name, {}).get(self.section_name, {})
            if not section_info:
                self.show_error("No data for this section!")
                self.page.go("/sections")
                self.page.update()
                return

            self.prepare_fields_list(section_info)
            self.current_field_index = 0
            self.show_current_field()

    def prepare_fields_list(self, section_info):
        self.fields_data = []

        for fname, fdata in section_info.get('numeric_fields', {}).items():
            rng = fdata.get('range', None)

            min_val = None
            max_val = None

            if isinstance(rng, (tuple, list)):
                if len(rng) >= 1:
                    min_val = rng[0]
                if len(rng) >= 2:
                    max_val = rng[1]
            elif isinstance(rng, (int, float)):
                min_val = rng

            self.fields_data.append({
                'type': 'numeric',
                'name': fname,
                'unit': fdata.get('unit', ''),
                'min': min_val,
                'max': max_val,
                'value': None
            })

        for fname, fdata in section_info.get('option_fields', {}).items():
            normal = fdata.get('normal') or (
                fdata.get('options')[0] if fdata.get('options') else ''
            )
            self.fields_data.append({
                'type': 'option',
                'name': fname,
                'options': fdata.get('options', []),
                'normal_option': normal,
                'value': None
            })

    def show_current_field(self):
        if self.current_field_index >= len(self.fields_data):
            self.save_all_data()
            return

        self.controls.clear()
        current = self.fields_data[self.current_field_index]
        self.create_field_ui(current)

    def create_field_ui(self, field):
        title = ft.Text(
            f"{self.device_name} → {self.section_name}",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=self.SKY_BLUE
        )

        progress_text = ft.Text(
            f"Field {self.current_field_index + 1} of {len(self.fields_data)}",
            size=15,
            color=ft.Colors.GREY_400
        )
        progress_bar = ft.ProgressBar(
            value=(self.current_field_index + 1) / len(self.fields_data),
            width=500,
            color=self.SKY_BLUE,
            bgcolor=ft.Colors.WHITE10
        )

        # نمایش رنج مجاز (همیشه)
        range_hint = ""
        if field['type'] == 'numeric':
            min_v = field.get('min')
            max_v = field.get('max')

            if min_v is not None and max_v is not None:
                range_hint = f"Normal range: {min_v} – {max_v} {field['unit']}"
            elif min_v is not None:
                range_hint = f"Normal ≥ {min_v} {field['unit']}"
            elif max_v is not None:
                range_hint = f"Normal ≤ {max_v} {field['unit']}"


        range_display = ft.Text(range_hint, color=ft.Colors.CYAN_300, size=14, italic=True)

        if field['type'] == 'numeric':
            self.numeric_input = ft.TextField(
                label=field['name'],
                hint_text=range_hint or "Enter value...",
                keyboard_type=ft.KeyboardType.NUMBER,
                border_color=self.SKY_BLUE,
                bgcolor=ft.Colors.WHITE10,
                color=self.TEXT_COLOR,
                width=350,
                text_size=22,
                text_align=ft.TextAlign.CENTER,
                on_change=self.on_numeric_change  # مهم: برای چک لحظه‌ای
            )
            self.validation_error = ft.Text("", size=16)  # خالی در ابتدا

            field_control = ft.Column([
                ft.Text(field['name'], size=20, weight=ft.FontWeight.BOLD, color=self.TEXT_COLOR),
                range_display,
                ft.Divider(height=8),
                self.numeric_input,
                self.validation_error
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

        else:
            normal = field.get('normal_option', '')
            normal_text = f"Normal value: {normal}" if normal else ""
            normal_display = ft.Text(normal_text, color=ft.Colors.GREEN_400, size=14, italic=True)

            self.radio_group = ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value=opt, label=opt, label_style=ft.TextStyle(color=self.TEXT_COLOR))
                    for opt in field['options']
                ]),
                on_change=self.on_option_change  # چک لحظه‌ای
            )
            self.option_warning = ft.Text("", size=15)

            field_control = ft.Column([
                ft.Text(field['name'], size=20, weight=ft.FontWeight.BOLD, color=self.TEXT_COLOR),
                normal_display,
                ft.Divider(height=8),
                self.radio_group,
                self.option_warning
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

        is_last = self.current_field_index == len(self.fields_data) - 1
        nav = ft.Row([
            ft.ElevatedButton(
                "Back to Sections" if self.current_field_index == 0 else "Previous",
                on_click=self.go_to_previous_field,
                bgcolor=ft.Colors.RED_400,
                color=ft.Colors.WHITE,
                width=180
            ),
            ft.ElevatedButton(
                "Finish & Save" if is_last else "Next",
                on_click=self.save_and_continue,
                bgcolor=ft.Colors.GREEN_500 if is_last else self.SKY_BLUE,
                color=ft.Colors.WHITE,
                width=180,
                icon=ft.Icons.CHECK_CIRCLE if is_last else ft.Icons.ARROW_FORWARD
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        self.controls = [
            title,
            progress_text,
            progress_bar,
            ft.Divider(height=30),
            field_control,
            ft.Divider(height=30),
            nav
        ]
        self.page.update()

    # چک لحظه‌ای برای عددی
    def on_numeric_change(self, e):
        value_text = e.control.value.strip()
        field = self.fields_data[self.current_field_index]

        if not value_text:
            self.validation_error.value = ""
            self.numeric_input.border_color = self.SKY_BLUE
            self.numeric_input.update()
            return

        try:
            value = float(value_text)
            min_v = field.get('min')
            max_v = field.get('max')

            if min_v is not None and value < min_v:
                self.validation_error.value = f"Below minimum ({min_v})"
                self.validation_error.color = ft.Colors.RED_ACCENT
                self.numeric_input.border_color = ft.Colors.RED_ACCENT

            elif max_v is not None and value > max_v:
                self.validation_error.value = f"Above maximum ({max_v})"
                self.validation_error.color = ft.Colors.RED_ACCENT
                self.numeric_input.border_color = ft.Colors.RED_ACCENT

            else:
                self.validation_error.value = "Within normal range"
                self.validation_error.color = ft.Colors.GREEN_400
                self.numeric_input.border_color = ft.Colors.GREEN_400

        except ValueError:
            self.validation_error.value = "Invalid number"
            self.validation_error.color = ft.Colors.RED
            self.numeric_input.border_color = ft.Colors.RED

        self.validation_error.update()
        self.numeric_input.update()

    # چک لحظه‌ای برای گزینه‌ای
    def on_option_change(self, e):
        selected = e.control.value
        field = self.fields_data[self.current_field_index]
        normal = field.get('normal_option')

        if not selected:
            self.option_warning.value = ""
            return

        if normal and selected != normal:
            self.option_warning.value = f"Unnormal (Normal: {normal})"
            self.option_warning.color = ft.Colors.ORANGE_ACCENT
        else:
            self.option_warning.value = "Normal"
            self.option_warning.color = ft.Colors.GREEN_400

        self.option_warning.update()

    def go_to_previous_field(self, e):
        if self.current_field_index == 0:
            self.page.go("/sections")
            self.page.update()
        else:
            self.current_field_index -= 1
            self.show_current_field()

    def save_and_continue(self, e):
        current = self.fields_data[self.current_field_index]

        if current['type'] == 'numeric':
            value_text = self.numeric_input.value.strip()
            if not value_text:
                self.validation_error.value = "Please enter a value"
                self.validation_error.color = ft.Colors.RED
                self.validation_error.update()
                return
            try:
                current['value'] = float(value_text)
            except:
                self.validation_error.value = "Invalid number"
                self.validation_error.update()
                return

        else:
            if not self.radio_group.value:
                self.option_warning.value = "Please select an option"
                self.option_warning.color = ft.Colors.RED
                self.option_warning.update()
                return
            current['value'] = self.radio_group.value

        # برو بعدی
        if self.current_field_index < len(self.fields_data) - 1:
            self.current_field_index += 1
            self.show_current_field()
        else:
            self.save_all_data()

    def save_all_data(self):
        form_data = self.page.session.get("form_data") or {}
        form_data.setdefault('sections', {})[self.section_name] = {
            f['name']: f['value'] for f in self.fields_data if f['value'] is not None
        }
        self.page.session.set("form_data", form_data)

        sb = ft.SnackBar(ft.Text(f"{self.section_name} saved successfully!"), bgcolor=ft.Colors.GREEN_700)
        self.page.overlay.append(sb)
        sb.open = True
        self.page.update()

        self.page.go("/sections")
        self.page.update()

    def show_error(self, msg):
        sb = ft.SnackBar(ft.Text(msg), bgcolor=ft.Colors.RED)
        self.page.overlay.append(sb)
        sb.open = True
        self.page.update()
