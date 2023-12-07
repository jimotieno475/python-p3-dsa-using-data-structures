class MyArray:
    def __init__(self):
        self.dictionary = {}
        self.length = 0

    def push(self, value):
        self.dictionary[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.dictionary.pop(self.length)

    def unshift(self, value):
        temp_dict = {}
        for i in range(self.length):
            temp_dict[i + 1] = self.dictionary[i]  # Shift elements to make space for the new value
        temp_dict[0] = value  # Add new value at the beginning
        self.dictionary = temp_dict
        self.length += 1

    def shift(self):
        if self.length == 0:
            return None
        shifted_value = self.dictionary[0]
        temp_dict = {}
        for i in range(1, self.length):
            temp_dict[i - 1] = self.dictionary[i]  # Shift elements to remove the first element
        self.dictionary = temp_dict
        self.length -= 1
        return shifted_value

arr = MyArray()
arr.push(1)
arr.push(2)
print(arr.pop())
arr.unshift(34)
arr.unshift(30)
arr.unshift(15)
print(arr.shift())
