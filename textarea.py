from nerodia.browser import Browser

br = Browser(browser="firefox")
br.goto("https://www.w3schools.com/html/html_form_elements.asp")
br.element(css="textarea[cols='30']").send_keys("hello world")
br.element(css="textarea[cols='30']").send_keys([COMMAND + 't'])

browser.close()
