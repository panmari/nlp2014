class MyDictionary:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.d = [None]*capacity
        self.used_slots = 0

    def insert(self, string):
        """insert(string): computes the hash of the string and adds it to the dictionary. If the string
        already exists, throws an Exception """
        pos = self.get_position(string)
        if self.d[pos] == string:
            raise '%s does already exist in dictionary!'.format(string)
        else:
            self.d[pos] = string
            self.used_slots += 1
            if self.used_slots > self.capacity/2:
                self.increase_size(2)


    def remove(self, string):
        """looks for the string by its hash value and removes it from the dictionary. If
        the string is not in the dictionary yet, throws an Exception"""
        pos = self.get_position(string)
        if self.d[pos] is None:
            raise '%s was not present in dictionary'.format(string)
        else:
            self.d[pos] = None
            self.used_slots -= 1

    def lookUp(self, string):
        """returns the string if in the dictionary, None otherwise"""
        pos = self.get_position(string)
        return self.d[pos]

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
        double_d = [None]*self.capacity
        old_d = self.d
        self.d = double_d
        # reinsert all entries into new dictionary
        for entry in old_d:
            if entry is not None:
                self.insert(entry)