def multiple_letter_count(string_value):
    newdict = dict.fromkeys(string_value,0)
    finaldict = { 
        key: string_value.count(key) for key in newdict
    }
    return finaldict

print(multiple_letter_count('Tanveer Tayeb'))