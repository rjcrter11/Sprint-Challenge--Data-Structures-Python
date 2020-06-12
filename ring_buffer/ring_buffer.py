class RingBuffer:
    def __init__(self, capacity):
        # Needs capacity(given value)
        # Something to store the values
        # Index to overwrite values when capacity is reached
        self.capacity = capacity
        self.index = 0
        self.storage = []

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            # If storage has reached capacity, data at the front needs to be overwritten
            # by index, which'll restart at 5 -- so  == capacity for restart
            self.storage[self.index] = item
            self.index += 1
            # print(self.index)
            if self.index == self.capacity:
                self.index = 0

    def get(self):
        return self.storage
