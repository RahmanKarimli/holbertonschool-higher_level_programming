import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Students: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
