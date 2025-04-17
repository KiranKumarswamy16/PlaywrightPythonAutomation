def test_select_dropdown_on_amazon_app(page, site_url):
    context, page = page
    page.select_option('//select[@id="searchDropdownBox"]', label='Baby')
    page.wait_for_timeout(3000)
    page.query_selector('//span[@id="nav-search-submit-text"]').click()
    page.wait_for_timeout(3000)
    page.get_by_text("Baby playtime", exact=False).is_visible()
    assert page.get_by_text("Baby playtime", exact=False).is_visible(), "'Baby playtime' not found!"
    print("'Baby playtime' text found! on baby page")
    page.wait_for_timeout(5000)
    page.close()



def test_mouse_hovering_on_amazon_app(page, site_url):
    context, page = page
    page.wait_for_selector('//span[text()="Hello, sign in"]').hover()
    page.wait_for_selector('//span[text()="Sign in"]').click()
    page.wait_for_timeout(2000)
    page.wait_for_selector('//input[@name="email"]').fill('8660355910')
    page.wait_for_selector('//span[@id="continue"]').click()
    page.wait_for_selector("//input[@class='a-input-text a-span12 auth-autofocus auth-required-field' and @name='password' and @id='ap_password' and @type='password']").fill('amazon@123')
    page.wait_for_selector('//input[@id="signInSubmit"]').click()
    page.wait_for_timeout(3000)
    page.get_by_text("Hello, Kiran", exact=False).is_visible()
    assert page.get_by_text("Hello, Kiran", exact=False).is_visible(), "'Hello, Kiran' not found!"
    print("'Hello, Kiran' text found! on Home page")
    page.wait_for_selector('//span[text()="Hello, Kiran"]').hover()
    page.wait_for_selector('//span[text()="Sign Out"]').click()
    page.wait_for_timeout(3000)
    page.get_by_text(" Sign in or create account", exact=False).is_visible()
    assert page.get_by_text("Sign in or create account", exact=False).is_visible(), "'Sign in or create account' not found!"
    print("'Sign in or create account' text found! on Sign In page")
    page.wait_for_timeout(5000)
    page.close()



def test_page_handling_on_amazon_app(page, site_url):
    context, page = page
    page.wait_for_selector('#twotabsearchtextbox').fill('iphone 16 e')
    page.wait_for_selector('#nav-search-submit-button').click()
    page.wait_for_selector('//span[text()="iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Ultramarine"]').click()
    page.wait_for_timeout(3000)
    total_pages = context.pages
    print(len(total_pages))
    new_page = total_pages[1]
    new_page.bring_to_front()
    new_page.wait_for_selector('// input[ @ id = "buy-now-button"]').click()
    new_page.wait_for_timeout(1000)
    new_page.wait_for_load_state('domcontentloaded')
    assert new_page.get_by_text("Sign in or create account",
                            exact=False).is_visible(), "'Sign in or create account' not found!"
    print("'Sign in or create account' text found! on Sign In page")
    new_page.close()
    page.bring_to_front()
    page.wait_for_timeout(5000)
    page.close()





