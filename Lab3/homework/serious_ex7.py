def remove_dollar_sign(text):
    text_fix = text.replace("$","")
    return text_fix

if __name__ == "__main__":
    text = input("enter a string: ")
    text_fix = remove_dollar_sign(text)
    print(text_fix)
