import empr

while True:
    text = input('empr >> ')
    result, error = empr.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
