@echo off
pytest -s testCases\test_checkbox_radiobutton_on_demotest_app_01.py --site=demoapp
pytest -s testCases\test_dialog_handles_on_internethero_app_02.py --site=internethero
pytest -s testCases\test_dropdown_mouseactions_windowhandling_on_amazon_app_03.py --site=amazon
pytest -s testCases\test_irames_on_paytm_app_04.py --site=paytm
