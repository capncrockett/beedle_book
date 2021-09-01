# old_macdonald.py

def old_mac():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"


def main_song(animal, sound):
    lyrics = f"{old_mac()}" \
             f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!\n" \
             f"With a {sound}, {sound} here and a {sound}, {sound} there. \n" \
             f"Here a {sound}, there a {sound}, " \
             f"everywhere a {sound}, {sound}. \n" \
             f"{old_mac()}"
    return lyrics


def main():
    animals = {
        "cow": "moo",
        "chicken": "cluck",
        "goat": "baa",
        "horse": "neigh",
        "dog": "woof",
    }
    for animal, sound in animals.items():
        print(main_song(animal, sound))


main()
