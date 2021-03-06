from typing import List
import os


version_file_content = """
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
# filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
# Set not needed items to zero 0.
filevers=(0, {version}, 0, 0),
prodvers=(0, 0, 0, 0),
# Contains a bitmask that specifies the valid bits 'flags'r
mask=0x0,
# Contains a bitmask that specifies the Boolean attributes of the file.
flags=0x0,
# The operating system for which this file was designed.
# 0x4 - NT and there is no need to change it.
OS=0x4,
# The general type of file.
# 0x1 - the file is an application.
fileType=0x1,
# The function of the file.
# 0x0 - the function is not defined for this fileType
subtype=0x0,
# Creation date and time stamp.
date=(0, 0)
),
  kids=[
StringFileInfo(
  [
  StringTable(
    u'040904B0',
    [StringStruct(u'CompanyName', u'{company_name}'),
    StringStruct(u'FileDescription', u'{file_description}'),
    StringStruct(u'FileVersion', u'{version}'),
    StringStruct(u'InternalName', u'{internal_name}'),
    StringStruct(u'LegalCopyright', u'{copyright}'),
    StringStruct(u'OriginalFilename', u'{original_filename}'),
    StringStruct(u'ProductName', u'{product_name}'),
    StringStruct(u'ProductVersion', u'{version}')])
  ]), 
VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""


class AppInfo:
    def __init__(self, a_app_name, a_company_name="", a_file_description="", a_version="", a_internal_name="",
                 a_copyright="", a_original_filename="", a_product_name=""):
        self.app_name = a_app_name
        self.company_name = a_company_name
        self.file_description = a_file_description
        self.version = a_version
        self.internal_name = a_internal_name
        self.copyright = a_copyright
        self.original_filename = a_original_filename
        self.product_name = a_product_name


def build_app(a_main_filename: str, a_app_info: AppInfo, a_distpath: str, a_icon_filename: str = "", a_noconsole=True,
              a_one_file=True, a_libs: List[str] = None):
    """
    ?????????????????? ???????????? ?????????? pyinstaller ?? ?????????????????? ??????????????????????.
    :param a_main_filename: ?????? ?????????? ???????????????? ??????????????
    :param a_app_info: ???????????????????? ?? ????????????????????
    :param a_distpath: ??????????, ?? ?????????????? ?????????? ?????????????????? ?????????????????? ????????????????????
    :param a_icon_filename: ???????? ?? ???????????? ????????????????????
    :param a_noconsole: ???????????????? noconole ?? pyinstaller
    :param a_one_file: ???????????????? onefile ?? pyinstaller
    :param a_libs: ???????????????????? (dll), ?????????????? ?????????? ???????????????? ?? ????????????
    """
    name = ' -n "{}"'.format(a_app_info.app_name)
    distpath = " --distpath {}".format(a_distpath) if a_distpath else ""
    onefile = " --onefile" if a_one_file else ""
    noconsole = " --noconsole" if a_noconsole else ""
    icon = " --icon={}".format(a_icon_filename) if a_icon_filename else ""
    add_data_sep = ";" if os.name == 'nt' else ":"
    libs = "".join((' --add-data "{}"{}.'.format(lib, add_data_sep) for lib in a_libs)) if a_libs is not None else ""

    version_filename = "version.txt"
    with open(version_filename, 'w', encoding="utf8") as version_file:
        version_file.write(version_file_content.format(
            company_name=a_app_info.company_name, file_description=a_app_info.file_description,
            version=a_app_info.version, internal_name=a_app_info.internal_name, copyright=a_app_info.copyright,
            original_filename=a_app_info.original_filename, product_name=a_app_info.product_name
        ))
        version = " --version-file={}".format(version_filename)

    build_cmd = "pyinstaller{}{}{}{}{}{}{} {}".format(
        name, distpath, onefile, noconsole, icon, version, libs, a_main_filename)
    os.system(build_cmd)

    os.remove(version_filename)
