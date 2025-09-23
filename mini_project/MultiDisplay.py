from dataclasses import dataclass


@dataclass
class MultiDisplay:
    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def to_string(self):
        return (f"Message: {self.message}, Count: {self.count}")

    def display(self):
        for c in range(self.count):
            print(self.message)

    def set_display(self, message, count):
        self.message = message
        self.count = count
        self.display()


