nuitka --onefile --standalone ^
--enable-plugin=pygame ^
--remove-output ^
--assume-yes-for-downloads ^
--lto=yes ^
--clang ^
--show-progress ^
--output-dir=build ^
--windows-disable-console ^
main.py
