// Time Complexity : O(1)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes

class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.bucketItems = 1000
        self.storage = [None]* self.buckets

    def add(self, key: int) -> None:
        bucket = key%1000
        bucketItem = int(key/1000)
        if self.storage[bucket] == None:
            self.storage[bucket]= [False]* self.bucketItems
        self.storage[bucket][bucketItem]= True
        return

    def remove(self, key: int) -> None:
        bucket = key%1000
        bucketItem = int(key/1000)
        if self.storage[bucket] == None:
            return
        self.storage[bucket][bucketItem]= False

    def contains(self, key: int) -> bool:
        bucket = key%1000
        bucketItem = int(key/1000)
        if self.storage[bucket] == None:
            return False
        elif self.storage[bucket][bucketItem] is not False:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)