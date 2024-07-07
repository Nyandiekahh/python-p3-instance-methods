#!/usr/bin/env python3

class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Test the Person class methods
if __name__ == "__main__":
    alice = Person()
    alice.talk()  # Should print: Hello World!
    alice.walk()  # Should print: The person is walking.

    bob = Person()
    bob.talk()  # Should print: Hello World!
    bob.walk()  # Should print: The person is walking.
