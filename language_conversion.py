convert_word_to_hindi = {
    "and" : "aur ",
    "1" : "ek ",
    "2" : "do ",
    "3": "teen ",
    "4": "chaar ", 
    "5" : "paanch ", 
    "6" : "chhah ",
    "7" : "saat ",
    "8": "aath ", 
    "9" : "nau ",
    "10": "das ",
    "20": "bees ",
    "50": "pachaas ",
    "100": "ek sau ",
    "200": "do sau ",
    "500": "paanch sau ",
    "2000": "do hazaar ",
    "rupees": "rupaye ",
    "notes": "ke not ",
    "note": "ka not ",
    "detected": "mila "
}

def convert_lang(text):
    res = ""
    if text == "Reload the page and try with another better image":
        res = "Page ko punah lod karo aur ek aur behatar chhavi ke saath prayaas karo"
    else:
        wordArr = list(text.split(' '))
        res = "is chhavi mein "
        for word in wordArr:
            w = word.lower()
            if w in convert_word_to_hindi:
                res += convert_word_to_hindi[w]
        res += "hai"
        
    return res
