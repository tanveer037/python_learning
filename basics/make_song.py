def make_song(lim=99, drinks='soda'):
    for num in range(lim, -1, -1):
        if num == 0:
            yield f"No more {drinks}! "
        elif num == 1:
            yield f"Only 1 bottle of {drinks} left!"
        else:
            yield f"{num} bottles of {drinks} on the wall "
            


kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
