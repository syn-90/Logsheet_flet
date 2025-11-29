import os
import shutil
import sys
from datetime import datetime
import openpyxl
from openpyxl.utils import get_column_letter

class ExcelHandler:
    def __init__(self, template_file='LOG SHEET 1.xlsx', save_dir='logs'):
        import sys, os
        import shutil

        # مسیر واقعی فایل template در حالت exe یا py
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        self.template_file = os.path.join(base_path, template_file)

        # --- مسیر کاملاً امن و بدون نیاز به permission ---
        try:
            app_dir = os.getcwd()  # مسیر sandbox برنامه در اندروید
            self.save_dir = os.path.join(app_dir, "GT11_Logs")
        except:
            # اگر به هر دلیلی، باز fallback به مسیر desktop برای ویندوز
            base_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
            self.save_dir = os.path.join(base_dir, 'logs')

        # ساخت مسیر
        os.makedirs(self.save_dir, exist_ok=True)

        # کپی‌کردن template
        try:
            src_template = os.path.join(os.path.dirname(__file__), 'templates', template_file)
            dst_template = os.path.join(self.save_dir, template_file)

            if os.path.exists(src_template) and not os.path.exists(dst_template):
                shutil.copy2(src_template, dst_template)
        except Exception as e:
            print("couldn't copy template:", e)

    def get_save_path(self):
        """ برمی‌گردونه مسیر فایل لاگ برای تاریخ امروز """
        today = datetime.today().strftime('%Y-%m-%d')
        filename = f"GT_Log_{today}.xlsx"
        return os.path.join(self.save_dir, filename)    
    def save_form_data(self, form_data):
        """ذخیره داده‌های فرم در اکسل - اگر فایل امروز وجود دارد به آن اضافه کن"""
        try:
            print("🔄A شروع فرآیند ذخیره‌سازی...")
            print(f"📋 Bداده‌های دریافتی: {form_data}")
            
            # بررسی وجود فایل template
            if not os.path.exists(self.template_file):
                print(f"❌ فایل template یافت نشد:C {self.template_file}")
                return False
            
            # ایجاد نام فایل خروجی با تاریخ امروز
            today = datetime.now().strftime("%Y-%m-%d")
            output_path = os.path.join(self.save_dir, f"GT_Log_{today}.xlsx")
            
            # بررسی اگر فایل امروز وجود دارد
            if os.path.exists(output_path):
                print(f"✅ فایل امروز موجود است: D{output_path}")
                print("📖 استفاده از فایل موجود و اضافه کردن داده‌های جدید...E")
                # از فایل موجود استفاده کن
                wb = openpyxl.load_workbook(output_path)
            else:
                print(f"📋 ایجاد فایل جدید برای امروز: F{output_path}")
                # ایجاد فایل جدید از روی template
                shutil.copy2(self.template_file, output_path)
                wb = openpyxl.load_workbook(output_path)
            
            device_name = form_data.get('device', 'General')
            print(f"📊 دستگاه انتخاب شده:G {device_name}")
            
            # انتخاب شیت مربوط به دستگاه
            if device_name in wb.sheetnames:
                ws = wb[device_name]
                print(f"✅ شیت H{device_name} پیدا شد")
            else:
                print(f"⚠ شیت I{device_name} یافت نشد، استفاده از اولین شیت")
                ws = wb[wb.sheetnames[0]]
            
            # پیدا کردن ستون زمان
            time_value = form_data.get('time', '0')
            print(f"⏰ زمان انتخاب شده:J {time_value}")
            
            time_col = self._find_time_column(ws, time_value)
            if time_col is None:
                print("❌ ستون زمان یافت نشدK")
                return False
            
            print(f"✅ ستون زمان:L {time_col}")
            
            # بررسی اگر این سلول قبلاً پر شده است
            existing_value = None
            try:
                # اینجا باید یک سلول نمونه را چک کنیم تا ببینیم قبلاً پر شده یا نه
                # مثلاً اولین فیلد از اولین بخش را چک می‌کنیم
                sections_data = form_data.get('sections', {})
                if sections_data:
                    first_section = list(sections_data.keys())[0]
                    first_field = list(sections_data[first_section].keys())[0]
                    
                    # پیدا کردن موقعیت فیلد
                    section_position = self._find_exact_section_position(ws, first_section)
                    if section_position:
                        field_column = self._find_field_column_near_section(ws, section_position)
                        if field_column:
                            field_row = self._find_exact_field_row(ws, first_field, section_position, field_column)
                            if field_row:
                                existing_value = ws.cell(row=field_row, column=time_col).value
            except:
                pass
            
            if existing_value is not None:
                print(f"M⚠ هشدار: سلول ({field_row}, {time_col}) قبلاً با مقدار '{existing_value}' پر شده است")
                print("📝 مقدار جدید جایگزین خواهد شد")
            
            # پردازش تمام بخش‌ها
            sections_data = form_data.get('sections', {})
            print(f"📝 بخش‌های برای پردازش: N{list(sections_data.keys())}")
            
            for section_name, fields in sections_data.items():
                print(f"\n🎯 شروع پردازش بخش: {section_name}")
                print(f"📋 فیلدهای این بخش: {list(fields.keys())}")
                
                # پیدا کردن موقعیت دقیق این بخش در اکسل
                section_position = self._find_exact_section_position(ws, section_name)
                
                if not section_position:
                    print(f"⚠ بخش {section_name} در اکسل یافت نشد")
                    continue
                
                print(f"✅ بخش {section_name} در سطر {section_position['section_row']}, ستون {section_position['section_col']} پیدا شد")
                
                # پیدا کردن ستون فیلدها برای این بخش
                field_column = self._find_field_column_near_section(ws, section_position)
                if not field_column:
                    print(f"⚠ ستون فیلدها برای بخش {section_name} یافت نشد")
                    continue
                
                print(f"✅ ستون فیلدها برای بخش {section_name}: {field_column}")
                
                # پردازش تمام فیلدهای این بخش
                for field_name, field_value in fields.items():
                    print(f"  📋 پردازش فیلد: {field_name} = {field_value}")
                    
                    # پیدا کردن سطر دقیق این فیلد در محدوده بخش
                    field_row = self._find_exact_field_row(ws, field_name, section_position, field_column)
                    
                    if field_row:
                        print(f"    ✅ سطر فیلد پیدا شد: {field_row}")
                        
                        # بررسی اگر سلول قبلاً پر شده
                        current_value = ws.cell(row=field_row, column=time_col).value
                        if current_value is not None:
                            print(f"    ⚠ سلول قبلاً با مقدار '{current_value}' پر شده بود")
                        
                        # ذخیره مقدار در سلول مناسب
                        ws.cell(row=field_row, column=time_col, value=field_value)
                        print(f"    ✅ مقدار {field_value} در سلول ({field_row}, {time_col}) ذخیره شد")
                    else:
                        print(f"    ❌ سطر برای فیلد {field_name} یافت نشد")
            
            # ذخیره‌ی کامنت در پایان شیت
            comment_text = form_data.get('comment', None)
            if comment_text:
                last_row = ws.max_row + 2  # دو سطر فاصله برای زیبایی
                ws.cell(row=last_row, column=1).value = "Comment:"
                ws.cell(row=last_row, column=2).value = comment_text
                print(f"📝 کامنت ذخیره شد در سطر {last_row}: {comment_text}")

            wb.save(output_path)
            print(f"✅ داده‌ها با موفقیت در {output_path} ذخیره شدند")
            
            # نمایش اطلاعات فایل
            file_size = os.path.getsize(output_path) / 1024  # به کیلوبایت
            print(f"📊 حجم فایل: {file_size:.2f} KB")
            print(f"🕒 زمان ذخیره‌سازی: {datetime.now().strftime('%H:%M:%S')}")
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در ذخیره داده‌ها: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    

    def check_existing_file(self, date_str=None):
        """بررسی اگر فایل با تاریخ مشخص وجود دارد"""
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        
        output_path = os.path.join(self.save_dir, f"GT_Log_{date_str}.xlsx")
        
        if os.path.exists(output_path):
            # اطلاعات فایل موجود
            file_size = os.path.getsize(output_path) / 1024
            mod_time = datetime.fromtimestamp(os.path.getmtime(output_path))
            
            print(f"✅ فایل موجود: {output_path}")
            print(f"📊 حجم: {file_size:.2f} KB")
            print(f"🕒 آخرین تغییر: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            return output_path, True
        else:
            print(f"❌ فایل برای تاریخ {date_str} یافت نشد")
            return output_path, False

    def get_worksheet(self, wb, device_name):
        """پیدا کردن شیت با تطبیق انعطاف‌پذیر نام"""
        try:
            # اول نام دقیق رو چک کن
            if device_name in wb.sheetnames:
                return wb[device_name]
            
            # اگر دقیق پیدا نشد، به صورت case-insensitive جستجو کن
            device_lower = device_name.lower()
            for sheet_name in wb.sheetnames:
                if sheet_name.lower() == device_lower:
                    return wb[sheet_name]
            
            # اگر هنوز پیدا نشد، جستجوی partial انجام بده
            for sheet_name in wb.sheetnames:
                if device_lower in sheet_name.lower():
                    print(f"✅ شیت مشابه پیدا شد: '{sheet_name}' برای دستگاه '{device_name}'")
                    return wb[sheet_name]
            
            # همه شیت‌ها رو برای دیباگ نمایش بده
            print(f"📋 تمام شیت‌های موجود: {wb.sheetnames}")
            return wb[wb.sheetnames[0]]
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن شیت: {e}")
            return wb[wb.sheetnames[0]]


    def _get_merged_cell_value(self, worksheet, row, col):
        for mr in worksheet.merged_cells.ranges:
            if mr.min_row <= row <= mr.max_row and mr.min_col <= col <= mr.max_col:
                return worksheet.cell(row=mr.min_row, column=mr.min_col).value
        return worksheet.cell(row=row, column=col).value


    def _find_exact_field_row(self, worksheet, field_name, section_position, field_column):
        """
        جستجو برای نام فیلد در ستون field_column؛
        شروع از همان ردیف section_position['section_row'] (در صورت قرار گرفتن فیلد روی همان ردیف)
        و استفاده از _get_merged_cell_value برای خواندن صحیح مقادیر merge شده.
        """
        try:
            section_row = section_position['section_row']
            mapped_name = self.map_field_name(field_name)
            search_str = str(mapped_name).lower()

            print(f"🔍 پیدا کردن فیلد '{field_name}' near بخش در سطر {section_row}")

            # از خود سطر بخش شروع کن (نه سطر بعدی)
            start_row = section_row
            end_row = min(section_row + 20, worksheet.max_row)  # محدودهٔ جستجو تا ۲۰ سطر پایین‌تر

            for row in range(start_row, end_row + 1):
                cell_value = self._get_merged_cell_value(worksheet, row, field_column)

                if cell_value:
                    cell_str = str(cell_value).lower()
                    if search_str in cell_str:
                        print(f"✅ فیلد '{mapped_name}' در سطر {row} پیدا شد: '{cell_value}'")
                        return row

            print(f"❌ فیلد '{field_name}' در محدوده بخش یافت نشد")
            return None

        except Exception as e:
            print(f"❌ خطا در پیدا کردن فیلد: {e}")
            return None

    def _find_exact_section_position(self, worksheet, section_name):
        """پیدا کردن موقعیت دقیق یک بخش در اکسل"""
        try:
            print(f"🔍 پیدا کردن موقعیت دقیق بخش: {section_name}")
            
            # ابتدا به دنبال نام دقیق بخش بگرد
            for row in range(1, worksheet.max_row + 1):
                for col in range(1, worksheet.max_column + 1):
                    cell_value = worksheet.cell(row=row, column=col).value
                    
                    if cell_value and str(cell_value).strip().lower() == section_name.lower():
                        print(f"✅ بخش {section_name} در سطر {row}, ستون {col} پیدا شد")
                        return {'section_row': row, 'section_col': col}
            
            # اگر نام دقیق پیدا نشد، به دنبال بخشی بگرد که شامل این نام باشد
            for row in range(1, worksheet.max_row + 1):
                for col in range(1, worksheet.max_column + 1):
                    cell_value = worksheet.cell(row=row, column=col).value
                    
                    if cell_value and section_name.lower() in str(cell_value).lower():
                        print(f"✅ بخش مشابه {section_name} در سطر {row}, ستون {col} پیدا شد: '{cell_value}'")
                        return {'section_row': row, 'section_col': col}
            
            print(f"❌ بخش {section_name} یافت نشد")
            return None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن موقعیت بخش: {e}")
            return None


    def _find_field_column_near_section(self, worksheet, section_position):
        """پیدا کردن ستون فیلدها در نزدیکی بخش"""
        try:
            section_row = section_position['section_row']
            section_col = section_position['section_col']
            
            print(f"🔍 پیدا کردن ستون فیلدها near بخش در سطر {section_row}")
            
            # معمولاً فیلدها در ستون‌های سمت راست بخش هستند
            # ابتدا ستون‌های مجاور را بررسی کن
            for col_offset in [1, 2, 3, -1, -2, -3]:  # راست و چپ را بررسی کن
                check_col = section_col + col_offset
                if 1 <= check_col <= worksheet.max_column:
                    cell_value = worksheet.cell(row=section_row, column=check_col).value
                    if cell_value and isinstance(cell_value, str) and len(cell_value.strip()) > 2:
                        print(f"✅ ستون فیلدها پیدا شد: {check_col} ('{cell_value}')")
                        return check_col
            
            # اگر در ردیف بخش پیدا نشد، در ردیف‌های پایین‌تر جستجو کن
            for row in range(section_row + 1, min(section_row + 10, worksheet.max_row + 1)):
                for col in range(1, min(10, worksheet.max_column + 1)):
                    cell_value = worksheet.cell(row=row, column=col).value
                    if cell_value and isinstance(cell_value, str) and len(cell_value.strip()) > 2:
                        # چک کن که این سلول مربوط به واحدها نباشد
                        unit_indicators = ['ºc', 'bar', 'v', 'a', 'kv', 'ka', 'mw', 'mbar', '%', 'ok/not ok', 'auto/manual']
                        if not any(indicator in str(cell_value).lower() for indicator in unit_indicators):
                            print(f"✅ ستون فیلدها پیدا شد: {col} در سطر {row} ('{cell_value}')")
                            return col
            
            print("❌ ستون فیلدها یافت نشد")
            return None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن ستون فیلدها: {e}")
            return None

    def debug_all_columns(self, worksheet, max_rows=20, max_cols=10):
        """دیباگ تمام ستون‌های مهم"""
        print("🔍 دیباگ تمام ستون‌های مهم:")
        
        for col in range(1, min(max_cols + 1, worksheet.max_column + 1)):
            print(f"\n📊 ستون {col}:")
            has_data = False
            
            for row in range(1, min(max_rows + 1, worksheet.max_row + 1)):
                cell_value = worksheet.cell(row=row, column=col).value
                if cell_value:
                    print(f"   سطر {row}: '{cell_value}'")
                    has_data = True
            
            if not has_data:
                print("   (بدون داده)")

    def map_field_name(self, field_name):
        """تطبیق نام فیلد با نام‌های موجود در اکسل"""
        field_mapping = {
            'battery voltage': 'Battery voltage',
            'coolant temp': 'coolant temp', 
            'level of fuel': 'Level of fuel',
            'leakage': 'Leakage',
            'dg model(local panel)': 'DG mode(Local panel)',
            'dg mode(local panel)': 'DG mode(Local panel)',
            'dg mode(8610)': 'DG mode(8610)',
            
            # برای سایر دستگاه‌ها
            'voltage': 'Voltage',
            'current': 'Current', 
            'temperature': 'Temperature',
            'pressure': 'Pressure',
            'level': 'Level',
            'status': 'Status'
        }
        
        lower_field = field_name.lower()
        return field_mapping.get(lower_field, field_name)

    def _find_field_row(self, worksheet, field_name):
        """پیدا کردن سطر مربوط به یک فیلد خاص"""
        try:
            print(f"🔍 جستجوی فیلد: '{field_name}'")
            
            # جستجو در تمام سطرها و ستون‌ها
            for row in range(1, worksheet.max_row + 1):
                for col in range(1, worksheet.max_column + 1):
                    cell_value = worksheet.cell(row=row, column=col).value
                    
                    if cell_value and str(field_name).lower() in str(cell_value).lower():
                        print(f"✅ فیلد '{field_name}' در سطر {row}, ستون {col} پیدا شد: '{cell_value}'")
                        return row
            
            print(f"❌ فیلد '{field_name}' در هیچ‌یک از سلول‌ها یافت نشد")
            return None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن سطر فیلد: {e}")
            return None

    def debug_time_row(self, worksheet):
        """برای دیباگ کردن سطر اول (زمان‌ها)"""
        print("🔍 دیباگ سطر اول (زمان‌ها):")
        
        time_row = 1
        row_data = []
        
        for col in range(1, worksheet.max_column + 1):
            cell_value = worksheet.cell(row=time_row, column=col).value
            if cell_value is not None:
                row_data.append(f"ستون {col}: '{cell_value}'")
        
        print(f"سطر 1: {', '.join(row_data)}")
        
        # نمایش کامل‌تر برای دیباگ
        print("\n📋 تمام سلول‌های سطر اول:")
        for col in range(1, worksheet.max_column + 1):
            cell_value = worksheet.cell(row=time_row, column=col).value
            print(f"ستون {col} ({get_column_letter(col)}): '{cell_value}'")

    def _find_time_column(self, worksheet, time_value):
        try:
            # تبدیل زمان به عدد (مثلاً "04:00" به 4)
            if ":" in str(time_value):
                time_num = int(time_value.split(":")[0])
            else:
                time_num = int(time_value)
            
            print(f"🔍 جستجوی زمان: {time_value} -> {time_num}")
            
            # زمان‌ها در سطر اول هستند (ردیف 1)
            time_row = 1
            
            # از ستون اول تا آخر جستجو کن
            for col in range(1, worksheet.max_column + 1):
                cell_value = worksheet.cell(row=time_row, column=col).value
                
                if cell_value is not None:
                    cell_str = str(cell_value)
                    print(f"   بررسی ستون {col}: '{cell_str}'")
                    
                    # چک کن اگر سلول حاوی عدد مورد نظر ما باشد
                    if str(time_num) in cell_str:
                        print(f"✅ ستون زمان پیدا شد: ستون {col} ('{cell_str}')")
                        return col
            
            print("❌ ستون زمان یافت نشد در سطر اول")
            return None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن ستون زمان: {e}")
            return None

    def find_field_column(self, worksheet):
        """پیدا کردن ستونی که شامل فیلدها است"""
        try:
            print("🔍 در حال پیدا کردن ستون فیلدها...")
            
            # بررسی 20 سطر اول و 10 ستون اول
            for col in range(1, min(11, worksheet.max_column + 1)):
                field_count = 0
                print(f"📊 بررسی ستون {col}:")
                
                for row in range(1, min(21, worksheet.max_row + 1)):
                    cell_value = worksheet.cell(row=row, column=col).value
                    if cell_value and isinstance(cell_value, str) and len(cell_value.strip()) > 3:
                        print(f"   سطر {row}: '{cell_value}'")
                        field_count += 1
                
                # اگر در این ستون چندین فیلد پیدا شد، احتمالاً ستون فیلدها است
                if field_count >= 3:  # حداقل 3 فیلد پیدا شده
                    print(f"✅ ستون فیلدها پیدا شد: ستون {col}")
                    return col
            
            print("❌ ستون فیلدها یافت نشد")
            return None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن ستون فیلدها: {e}")
            return None

    def _find_field_row(self, worksheet, field_name, field_column=None):
        """پیدا کردن سطر مربوط به یک فیلد خاص"""
        try:
            # اگر ستون فیلدها مشخص نیست، آن را پیدا کن
            if field_column is None:
                field_column = self.find_field_column(worksheet)
                if field_column is None:
                    print("❌ ستون فیلدها یافت نشد")
                    return None
            
            print(f"🔍 جستجوی فیلد: '{field_name}' در ستون {field_column}")
            
            # تطبیق نام فیلد
            mapped_name = self.map_field_name(field_name)
            search_str = str(mapped_name).lower()
            
            # در ستون فیلدها جستجو کن
            for row in range(1, worksheet.max_row + 1):
                cell_value = worksheet.cell(row=row, column=field_column).value
                
                if cell_value:
                    cell_str = str(cell_value).lower()
                    
                    if search_str in cell_str:
                        print(f"✅ فیلد '{mapped_name}' در سطر {row} پیدا شد: '{cell_value}'")
                        return row, field_column
            
            print(f"❌ فیلد '{mapped_name}' در ستون {field_column} یافت نشد")
            return None, field_column
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن سطر فیلد: {e}")
            return None, field_column

    def _find_sections_for_device(self, worksheet, device_row, device_col):
        """پیدا کردن تمام بخش‌های یک دستگاه"""
        try:
            print(f"🔍 پیدا کردن بخش‌های دستگاه در سطر {device_row}")
            
            sections = []
            current_section = None
            
            # از سطر دستگاه به بعد رو بررسی کن
            for row in range(device_row + 1, worksheet.max_row + 1):
                # سلول همستون با دستگاه رو بررسی کن (معمولاً بخش‌ها در همین ستون هستند)
                section_cell = worksheet.cell(row=row, column=device_col).value
                
                if section_cell and section_cell.strip():
                    # اگر سلول خالی نیست، ممکنه یک بخش جدید باشه
                    if not current_section or section_cell != current_section['name']:
                        current_section = {
                            'name': section_cell,
                            'start_row': row,
                            'end_row': None,
                            'field_column': None
                        }
                        sections.append(current_section)
                        print(f"✅ بخش جدید پیدا شد: {section_cell} در سطر {row}")
                
                # اگر بخش جاری داریم، ستون فیلدهای اون رو پیدا کن
                if current_section and current_section['field_column'] is None:
                    field_col = self._find_field_column_for_row(worksheet, row)
                    if field_col:
                        current_section['field_column'] = field_col
                        print(f"✅ ستون فیلدها برای بخش {current_section['name']}: {field_col}")
            
            return sections
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن بخش‌ها: {e}")
            return []

    def _find_device_position(self, worksheet, device_name):
        """پیدا کردن موقعیت دستگاه در شیت"""
        try:
            print(f"🔍 پیدا کردن موقعیت دستگاه: {device_name}")
            
            for row in range(1, worksheet.max_row + 1):
                for col in range(1, worksheet.max_column + 1):
                    cell_value = worksheet.cell(row=row, column=col).value
                    
                    if cell_value and device_name.lower() in str(cell_value).lower():
                        print(f"✅ دستگاه {device_name} در سطر {row}, ستون {col} پیدا شد: '{cell_value}'")
                        return row, col
            
            print(f"❌ دستگاه {device_name} یافت نشد")
            return None, None
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن دستگاه: {e}")
            return None, None

    def find_device_structure(self, worksheet, device_name):
        """پیدا کردن ساختار سلسله مراتبی دستگاه و بخش‌های آن"""
        try:
            print(f"🔍 پیدا کردن ساختار دستگاه: {device_name}")
            
            device_row, device_col = self._find_device_position(worksheet, device_name)
            if not device_row:
                print(f"❌ دستگاه {device_name} یافت نشد")
                return None
            
            print(f"✅ دستگاه {device_name} در سطر {device_row}, ستون {device_col} پیدا شد")
            
            # پیدا کردن تمام بخش‌های این دستگاه
            sections = self._find_sections_for_device(worksheet, device_row, device_col)
            
            return {
                'device_row': device_row,
                'device_col': device_col,
                'sections': sections
            }
            
        except Exception as e:
            print(f"❌ خطا در پیدا کردن ساختار دستگاه: {e}")
            return None

    def _save_operator_info(self, worksheet, form_data):
        """ذخیره اطلاعات اپراتورها در اکسل"""
        try:
            operator_info = {
                'shift': form_data.get('shift', ''),
                'shift_leader': form_data.get('shift_leader', ''),
                'shift_engineer': form_data.get('shift_engineer', ''),
                'date': form_data.get('date', '')
            }
            
            # اطلاعات معمولاً در سطرهای 1-5 قرار می‌گیرند
            for row in range(1, 6):
                cell_value = worksheet.cell(row=row, column=1).value
                
                if cell_value:
                    cell_str = str(cell_value).lower()
                    
                    if 'shift' in cell_str and 'engineer' not in cell_str:
                        worksheet.cell(row=row, column=2).value = operator_info['shift']
                    elif 'leader' in cell_str:
                        worksheet.cell(row=row, column=2).value = operator_info['shift_leader']
                    elif 'engineer' in cell_str:
                        worksheet.cell(row=row, column=2).value = operator_info['shift_engineer']
                    elif 'date' in cell_str:
                        worksheet.cell(row=row, column=2).value = operator_info['date']
                        
            print("✅ اطلاعات اپراتورها ذخیره شد")
                
        except Exception as e:
            print(f"⚠ خطا در ذخیره اطلاعات اپراتورها: {e}")

    def _check_field_status(self, device, section_name, field_name, field_value):
        """بررسی اینکه مقدار فیلد در محدوده مجاز است یا نه"""
        try:
            # این بخش باید با توجه به ساختار device_sections_map شما تنظیم شود
            # فعلاً یک نمونه ساده پیاده‌سازی می‌کنم
            
            # اگر مقدار خالی است، OK در نظر بگیر
            if field_value is None or field_value == "":
                return 'OK'
                
            # برای مقادیر عددی، بررسی محدوده
            try:
                numeric_value = float(field_value)
                # اینجا می‌توانید محدوده‌های خاص هر فیلد را بررسی کنید
                # به عنوان مثال ساده:
                if numeric_value < 0:
                    return 'ERROR'
            except ValueError:
                # اگر مقدار عددی نبود، OK در نظر بگیر
                pass
                
            return 'OK'
            
        except Exception as e:
            print(f"⚠ خطا در بررسی وضعیت فیلد: {e}")
            return 'OK'

