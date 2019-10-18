class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) == self.capacity:
      #remove item
      del self.storage[self.current]
      #insert new item at current index
      self.storage.insert(self.current, item)
      #increment current
      if self.current == self.capacity - 1:
        self.current = 0
      else:
        self.current += 1
    else: 
    # insert at end of list
      self.storage.append(item)


  def get(self):
    clean_list = [i for i in self.storage if i]
    return clean_list