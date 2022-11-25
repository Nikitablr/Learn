
def get_link(browser_chrome, browser_firefox):
    browser_chrome.get("https://github.com/")
    browser_firefox.get("https://github.com/")

def test(browser_chrome, browser_firefox):
    get_link(browser_chrome, browser_firefox)

