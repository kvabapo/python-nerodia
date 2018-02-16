from nerodia.browser import Browser

#launch browser and go to webpage
browser = Browser(browser='firefox')
browser.goto("http://toolsqa.com/automation-practice-form/")

#verify webpage title
if browser.title == "http://toolsqa.com/automation-practice-form/":
    print(browser.title)

#printout a text of the webpage
text1 = browser.element(class_name='h1-size')
if text1.text == "Automation Practice Form":
    print(text1.text)

browser.quit()
