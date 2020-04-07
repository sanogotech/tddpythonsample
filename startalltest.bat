rem start all tests
rem set PYTHONPATH=%PYTHONPATH%;path to the project root folder
rem  set for windows and export for linux
set PYTHONPATH=%PYTHONPATH%;.
pytest  -v -s  tests