from setuptools import setup, find_packages

setup(
    name='pyqt-dark-calculator',
    version='0.6.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_calculator.ico': ['calculator.svg'],
                  'pyqt_dark_calculator.style': ['calculator_pad_button.css']},
    description='PyQt dark calculator',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    setup_requires=[
        'wheel>=0.34.2'
    ],
    install_requires=[
        'pyinstaller>=5.1',
        'PyQt5>=5.15',
        'pyqt-style-setter>=0.0.1',
        'pyqt-resource-helper>=0.0.1',
        'absresgetter>=0.0.1',
        'pyqt-new-window-handler>=0.0.1'
    ]
)
