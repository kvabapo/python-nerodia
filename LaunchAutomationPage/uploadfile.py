from nerodia.browser import Browser

b = Browser(browser='chrome')
b.goto("http://toolsqa.com/automation-practice-form/")
print(b.title)

uploadfile = "/Users/Kerrrlo/Downloads/Photos/boss.jpeg"
b.file_field(id="photo").set(uploadfile)
