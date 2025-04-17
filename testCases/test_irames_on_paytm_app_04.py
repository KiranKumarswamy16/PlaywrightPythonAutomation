def test_click_links_in_iframe(page, site_url):
    context, page = page
    page.locator('//span[text()="Sign In"]').click()
    page.wait_for_timeout(5000)
    iframe = page.frame(name="oauth-iframe")
    iframe.locator('a[href="https://p.paytm.me/xCTH/adidwlsios"]').click()
    page.wait_for_timeout(3000)
    total_pages = context.pages
    new_page = total_pages[1]
    new_page.bring_to_front()
    new_page.wait_for_timeout(1000)
    assert new_page.get_by_text("Paytm: Secure UPI Payments",
                                exact=False).is_visible(), "'Paytm: Secure UPI Payments' text not found!"
    print("'Paytm: Secure UPI Payments' text found! on Paytm New Window Page")
    new_page.close()
    page.bring_to_front()
    page.wait_for_timeout(2000)
    page.wait_for_selector('//img[@alt="close"]').click()
    page.wait_for_timeout(2000)
    assert page.get_by_text("Search Flights",
                                exact=False).is_visible(), "'Search Flights' not found!"
    print("'Search Flights' text found! on Paytm Home Page")
    page.wait_for_timeout(5000)
    page.close()
