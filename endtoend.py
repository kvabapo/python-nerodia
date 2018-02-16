# coding=utf-8
from nerodia.browser import Browser

browser = Browser(browser="firefox")
browser.goto("http://toolsqa.com/automation-practice-form/")

if browser.title == "Demo Form for practicing Selenium Automation":
    print(browser.title)



text1 = browser.element(class_name="h1-size")
print(text1)

text2 = browser.element(
    css="#content > div.vc_row.wpb_row.vc_row-fluid.dt-default > div > div > div > div.vc_message_box.vc_message_box-standard.vc_message_box-rounded.vc_color-info > p:nth-child(2) > em > strong")
print(text2)

text3 = browser.element(
    text="Always click on the ads display at the right side, this is how we manage the website’s expenses and bring free content for the beginners.")
print(text3.text)


browser.link(text="Partial Link Test").wait_until_present().click()
browser.link(text="Link Test").wait_until_present().click()
browser.back()

browser.text_field(name="firstname").wait_until_present().set("Fname")
browser.text_field(name="firstname").clear()
browser.select_list(id="continents").select("Antartica")
browser.select_list(id="selenium_commands").select("Switch Commands")
browser.button(id="submit")

browser.radio(id="sex-0").set()
browser.radio(id="sex-1").set()
browser.radio(id="exp-2").set()
browser.text_field(id="datepicker").set("mmddyy")
browser.checkbox(value="Automation Tester").set()
browser.checkbox(id="profession-0").set()

browser.link(text="Test File to Download").click()
browser.checkbox(id="tool-0").set()
browser.checkbox(id="tool-0").clear()
browser.checkbox(id="tool-2").set()

browser.close()
