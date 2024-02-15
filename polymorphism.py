# Matthew Kusto
# 5/10/2023
# Week 5: Language Polymorphism
# CSIS-126E-1157


class Greeting:
    def english_hello(self):
        print("Hello")

    def english_bye(self):
        print("Goodbye")

    def arabic_hello(self):
        print("مرحبًا (mrhban)")

    def arabic_bye(self):
        print("مع السلامة (mae alsalama)")

    def german_hello(self):
        print("Hallo")

    def german_bye(self):
        print("Verabschiedung")


print("Main Menu")
print("A. English")
print("B. Arabic")
print("C. German")


main = input("Select a language: ")
lang = Greeting()

if main == "a":
    choice = input("Hello or Bye (h/b)?: ").upper()

    if choice == "H":
        lang.english_hello()

    elif choice == "B":
        lang.english_bye()

elif choice == "b":
    choice = input("Hello or Bye (h/b)?: ").upper()
    if choice == "H":
        lang.arabic_hello()

    elif choice == "B":
        lang.arabic_bye()

elif choice == "c":
    choice = input("Hello or Bye (h/b)?: ").upper()
    if choice == "H":
        lang.german_hello()

    elif choice == "B":
        lang.german_bye()

else:
    print("Invalid choice")
