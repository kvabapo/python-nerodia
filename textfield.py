from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto("http://toolsqa.com/automation-practice-form/")
print(browser.title)



browser.text_field(name="firstname").clear()
browser.text_field(name="lastname").clear()
browser.text_field(name="firstname").set("Fname")
browser.text_field(name="lastname").set("Lname")

browser.close()
