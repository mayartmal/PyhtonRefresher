class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        else:
            print(f"Printing {pages} pages")
            self.remaining_pages -= pages


# printer = Device("HP Printer", "LAN")
# print(printer)
# printer.disconnect()

printer = Printer("HP printer", "LAN", 500)
print(printer)
printer.print(20)
print(printer)
print()
printer.disconnect()


print()
printer.print(20)
