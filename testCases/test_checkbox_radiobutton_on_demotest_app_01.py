def test_select_checkbox_on_automation_demo_app(page, site_url):
    context, page = page
    cricket_checkbox = page.query_selector('//input[@value="Cricket"]')
    cricket_checkbox.check()
    assert cricket_checkbox.is_checked(), "Cricket checkbox not checked!"
    print("Cricket checkbox checked")
    page.wait_for_timeout(5000)
    hockey_checkbox = page.query_selector('//input[@value="Hockey"]')
    hockey_checkbox.check()
    assert hockey_checkbox.is_checked(), "Hockey checkbox not checked!"
    print("Hockey checkbox checked")
    page.wait_for_timeout(5000)
    movies_checkbox = page.query_selector('//input[@value="Movies"]')
    movies_checkbox.check()
    assert movies_checkbox.is_checked(), "Movies checkbox not checked!"
    print("Movies checkbox checked")
    page.wait_for_timeout(5000)
    page.close()


def test_radiobutton_on_automation_demo_app(page, site_url):
    context, page = page
    male_radio = page.wait_for_selector('//input[@value="Male"]')
    male_radio.check()
    assert male_radio.is_checked(), "Male radio button not checked!"
    print("Male radio button checked")
    page.wait_for_timeout(5000)
    female_radio = page.wait_for_selector('//input[@value="FeMale"]')
    female_radio.click()
    assert female_radio.is_checked(), "Female radio button not checked!"
    print("Female radio button checked")
    page.wait_for_timeout(5000)
    page.close()
