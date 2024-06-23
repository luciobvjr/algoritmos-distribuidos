class LamportClock:
  def __init__(self):
    self.logical_clock = 0

  def increment(self):
    """Increments the logical clock by 1."""
    self.logical_clock += 1

  def update(self, received_timestamp):
    """Updates the logical clock based on a received timestamp."""
    self.logical_clock = max(self.logical_clock, received_timestamp) + 1

  def get_timestamp(self):
    """Returns the current logical clock value."""
    return self.logical_clock

class Message:
    def __init__(self, content, timestamp):
        self.content = content
        self.timestamp = timestamp
    
    def __str__(self):
        return f"Message(content='{self.content}', timestamp={self.timestamp})"