#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Test the Dog class methods
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Should print: Woof!
    fido.sit()   # Should print: The dog is sitting.

    snoopy = Dog()
    snoopy.bark()  # Should print: Woof!
    snoopy.sit()   # Should print: The dog is sitting.
