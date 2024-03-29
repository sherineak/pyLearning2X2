# match case example

browser = str(input("Enter your browser \n"))
# browser = browser.lower()
match browser:
    case "CHROME":
        print("Your Chrome browser executed")
    case "Firefox":
        print("Your fire fox executed")
    case _:
        print("No browser found")