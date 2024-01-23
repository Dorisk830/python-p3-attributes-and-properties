#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
# Name must be str and btw 1-25 char
# breed property
class Dog:    
    def __init__(self, name="name", breed="Corgi" ):        
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name     

    def set_name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 25):
            self._name = new_name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed
        
    def set_breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self._breed = new_breed

        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)