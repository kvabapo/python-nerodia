from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto("http://toolsqa.com/automation-practice-form/")
print(browser.title)


text1 = browser.element(class_name='h1-size')
print(text1.text)

browser.radio(id="sex-0").set()
browser.radio(id="sex-1").set()
browser.radio(id="exp-2").set()

browser.close()
