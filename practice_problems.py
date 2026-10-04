"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    # A set is a good choice because it stores unique values and allows
    # fast membership checks. Checking if an item is in a set is O(1)
    # on average, so the complete solution runs in O(n) time.
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


"""
Problem 2: Order Manager

Maintain tasks in the order they were added and remove tasks from the front.
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        # A deque works well because this problem follows FIFO order.
        # Adding to the end and removing from the front are both O(1)
        # operations, making it more efficient than a normal list.
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None

        return self.tasks.popleft()


"""
Problem 3: Unique Value Counter

Track integer values and return the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        # A set is the best choice because it automatically stores only
        # unique values. Adding a value is O(1) on average, and getting
        # the number of unique values is also O(1).
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Simple tests

print(has_duplicates([10, 20, 30, 20, 40]))  # True
print(has_duplicates([1, 2, 3, 4, 5]))        # False

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())         # Email follow-up

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())              # 2