# coding:utf-8
# hash 函数实现简单的余数方法。冲突解决技术是 加1 rehash 函数的线性探测


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
# 重载 __getitem__ 和__setitem__ 方法以允许使用 [] 访问
# H[54] = 'cat' 调用的是__setitem__()

H = HashTable()
H[54] = 'cat'
H[26] = 'dog'
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print H.slots

print H.data

H[20] = 'duck'
print H.data
print H[99]

# 对于使用具有线性探测的开放寻址的成功搜索，平均比较数大约为1/2（1 + 1/(1-λ)），
# 不成功的搜索为 1/2(1+(1/1-λ)^2 )
# 如果我们使用链接，则对于成功的情况，平均比较数目是 1+λ/2，
# 如果搜索不成功，则简单地是 λ 比较次数。

