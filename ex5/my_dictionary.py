# comment out this line to try pythons own hash method

from ex5.ex1 import hash

class MyDictionary:

    def __init__(self, capacity=100):
        """This is basically a list of empty lists"""
        self.capacity = capacity
        self._initialize()

    def _initialize(self):
        """Makes a new list that matches the capacity of self.capacity and sets everything relevant to zero."""
        self.d = [[] for x in range(self.capacity)]
        self.used_slots = 0
        self.entries = 0

    def insert(self, string):
        """insert(string): computes the hash of the string and adds it to the dictionary. If the string
        already exists, throws an Exception """
        pos = self.get_position(string)
        pos_list = self.d[pos]
        if string in pos_list:
            raise KeyError('{} does already exist in dictionary!'.format(string))
        else:
            if len(pos_list) == 0: # was empty before
                self.used_slots += 1
            pos_list.append(string)
            self.entries += 1
            if self.used_slots > self.capacity/2:
                self.increase_size(2)

    def remove(self, string):
        """looks for the string by its hash value and removes it from the dictionary. If
        the string is not in the dictionary yet, throws an Exception"""
        pos = self.get_position(string)
        if not string in self.d[pos]:
            raise KeyError('{} was not present in dictionary'.format(string))
        else:
            self.d[pos].remove(string)
            self.entries -= 1
            if len(self.d[pos]) == 0:
                self.used_slots -= 1

    def lookUp(self, string):
        """returns the string if in the dictionary, None otherwise"""
        pos = self.get_position(string)
        if string in self.d[pos]:
            return string
        else:
            return None

    def get_position(self, string):
        return hash(string) % self.capacity

    #Note: this should rather be __sizeof__(self):
    def size(self):
        """returns the number of slots used (hash values in the dictionary)"""
        return self.used_slots

    def capacity(self):
        return self.capacity

    def increase_size(self, factor):
        """Multiplies the capacity of the dictionary by factor (usually 2)"""
        self.capacity *= factor
        old_d = self.d
        self._initialize()
        # reinsert all entries into new dictionary
        for list in old_d:
            for entry in list:
                self.insert(entry)