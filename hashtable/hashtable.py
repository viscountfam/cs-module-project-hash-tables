class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, prev=None, next_up=None):
        self.key = key
        self.value = value
        self.next = next_up
        self.prev = prev
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it as the new head of the list.
    Don't forget to handle the old head node's previous pointer accordingly.

    """

    def add_to_head(self, key, value):
        # create instance of Listnode with a value
        new_list_node = HashTableEntry(key, value)
        # increment the DLL length attribute
        self.length += 1
        
        #check if DLL is empty
            # if so set head and tail to the new node instance

        # if DLL is not empty
        if self.head is not None:
                # set new node's next to current head
            new_list_node.next = self.head
                # set head's prev to new node
            self.head.prev = new_list_node
                # set head to the new node
            self.head = new_list_node
        else:
            self.head = new_list_node
            self.tail = new_list_node

    def add_to_tail(self, key, value):
        # create instance of ListNode with a value
        new_list_node = HashTableEntry(key, value)
        # increment the DLL length attribute
        self.length += 1
        # check to see is DLL is empty
        if self.head is not None:
            # Assign the newly created node to the current tail's next
            self.tail.next = new_list_node
            # Assign the current tail to the newly created node's prev
            new_list_node.prev = self.tail
            # Assign self.tail to the newly created node
            self.tail = new_list_node
        else:
            self.head = new_list_node
            self.tail = new_list_node

    def remove_from_head(self):
        if self.head:
            value = self.head.value
        else:
            value = None
        self.delete(self.head)
        return value

    def remove_from_tail(self):
        if self.tail:
            value = self.tail.value
        else: 
            value = None
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the List and inserts is as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)


    """
    Remove the input node from its current spot in the List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the order of the other elements of the List.
    """
    def delete(self, node):
        # the logic here should be the same as move to end and move to start without the head and tail adjustments
        # if empty
        if not self.head and not self.tail:
            return None
        #if head and tail
        if node == self.head and self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes in the list.

    """
    def get_max(self):
        maximum = 0
        current = self.head
        while current is not None:
            if current.value > maximum:
                maximum = current.value
            current = current.next
        return maximum


    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return 
    
    def update_or_insert_at_head(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        
        self.add_to_head(key, value)
    
    def update_or_insert_at_tail(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        
        self.add_to_tail(key, value)

    def find_and_delete(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                self.delete(current)
        
        return None



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        # Your code here
        self.capacity = capacity
        self.table = [None for i in range(self.capacity)]
        self.load = 0
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0
        for index in self.table:
            if index:
                count += 1
        print(self.load/self.get_num_slots())
        return count/self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed_var = FNV_offset_basis

        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b
        
        return hashed_var

    def should_resize(self):
        if self.get_load_factor() >= .70:
           self.resize(self.capacity * 2)
        elif self.get_load_factor() <= .20:
            new_capacity = self.capacity/2
            if self.capacity/2 < 8:
                new_capacity = 8
            
            self.resize(new_capacity)
        else:
            return "Resize not yet necessary"

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_var = 5381
        for x in key:
            hash_var = (hash_var * 33) + ord(x)
        return hash_var


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.table[self.hash_index(key)] is None:
            self.table[self.hash_index(key)] = DoublyLinkedList(HashTableEntry(key, value))
            self.load += 1
        else:
            if self.table[self.hash_index(key)].find(key):
                self.table[self.hash_index(key)].update_or_insert_at_tail(key, value)
            else:
                self.table[self.hash_index(key)].add_to_tail(key,value)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        
        if self.table[self.hash_index(key)]:
            if self.table[self.hash_index(key)].head.key == key:
                self.table[self.hash_index(key)].delete(self.table[self.hash_index(key)].head)
            elif self.table[self.hash_index(key)].tail.key == key:
                self.table[self.hash_index(key)].delete(self.table[self.hash_index(key)].tail)
            else:
                self.table[self.hash_index(key)].find_and_delete(key)
        else:
            print("There is no value stored here")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        if self.table[self.hash_index(key)]:
            if self.table[self.hash_index(key)].head == key:
                return self.table[self.hash_index(key)].head
            elif self.table[self.hash_index(key)].tail == key:
                return self.table[self.hash_index(key)].tail
            else:
                return self.table[self.hash_index(key)].find(key)
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        temp = []
        # create a new table
        newTable = [None for i in range(new_capacity)]
        # loop through the old table
        for element in self.table:
            # if the array is populated
            if element:
                # loop through those key and values storing them
                    current = element.head
                    while current is not None:
                        temp.append([current.key, current.value])
                        current = current.next        
        self.table = newTable
        self.capacity = new_capacity
        # put those stored values back into the hash table
        for item in temp:
            self.put(item[0], item[1])
                
            
# hashed = HashTable(10)
# hashed.put("Name", "Michael Famurewa")
# print(hashed.get("Name"))
# hashed.put("Name", "Michael Jordan")
# print(hashed.get("Name"))
# hashed.put("fruit", "Apples")
# print(hashed.get("fruit"))
# hashed.put("watch", "this")
# print(hashed.table)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
