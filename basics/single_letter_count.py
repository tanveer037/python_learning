def single_letter_count(string,letter):
    value = string.upper().count(letter.upper())
    return value

print(single_letter_count("My name is Tanveer Tayeb",'t'))