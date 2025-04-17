def test_dialogs_alerts_handling_on_internethero_app(page, site_url):
    context, page = page
    page.wait_for_selector("//button[text()='Click for JS Confirm']").click()
    page.on("dialog", lambda dialog: dialog.dismiss())
    assert page.get_by_text("You clicked: Cancel",
                                exact=False).is_visible(), "'You clicked: Cancel' not found!"
    print("'You clicked: Cancel' text found! on Dialog page")
    page.wait_for_timeout(4000)
    page.wait_for_selector("//button[text()='Click for JS Prompt']").click()
    page.on("dialog", lambda dialog: dialog.dismiss())
    assert page.get_by_text("You entered: null",
                                exact=False).is_visible(), "'You entered: null' not found!"
    print("'You entered: null' text found! on Dialog page")
    page.wait_for_timeout(4000)
    page.wait_for_selector("//button[text()='Click for JS Alert']").click()
    page.on("dialog", lambda dialog: dialog.accept())
    assert page.get_by_text("You successfully clicked an alert",
                            exact=False).is_visible(), "'You successfully clicked an alert' not found!"
    print("'You successfully clicked an alert' text found! on Dialog page")
    page.wait_for_timeout(5000)
    page.close()