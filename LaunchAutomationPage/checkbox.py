from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto("http://toolsqa.com/automation-practice-form/")
print(browser.title)

#select a checkbox
browser.checkbox(id="tool-0").set()
#deseclect a checkbox
browser.checkbox(id="tool-0").clear()

browser.close()
