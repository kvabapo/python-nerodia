from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto("http://toolsqa.com/automation-practice-form/")
print(browser.title)


browser.link(text="Test File to Download").click()

browser.close()
