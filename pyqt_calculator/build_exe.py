from typing import List, Tuple
import re

import pyinstaller_build as py_build
from pyqt_dark_calculator import app_info


if __name__ == "__main__":
    app_info = py_build.AppInfo(a_app_name=app_info.SHORT_NAME,
                                a_version=app_info.VERSION,
                                a_company_name='',
                                a_file_description=app_info.FULL_NAME,
                                a_internal_name=app_info.SHORT_NAME,
                                a_copyright='',
                                a_original_filename=app_info.FULL_NAME,
                                a_product_name=app_info.FULL_NAME)

    libs = [
        # 'C:\\Windows\\System32\\vcruntime140d.dll',
        # 'C:\\Windows\\System32\\ucrtbased.dll',
    ]

    py_build.build_app(a_main_filename="calculator.py",
                        a_app_info=app_info,
                        a_distpath="../bin",
                        a_noconsole=False,
                        a_one_file=True,
                        a_libs=libs)
