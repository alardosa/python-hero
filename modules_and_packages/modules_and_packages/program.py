from module import hello

hello('Al Ardosa')
# output: Hello Al Ardosa

from package.main import report_main
from package.subpackage.submain import report_submain

report_main()
# output: Hey Im report_main function inside package > main.py

report_submain()
# output: Hey Im report_submain function inside subpackage > submain.py
