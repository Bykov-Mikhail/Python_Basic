class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
             self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def __str__(self):
        if self.head is None:
            return '[]'
        main = []
        current = self.head
        while current is not None:
            main.append(str(current.data))
            current = current.next
        return '[' + ', '.join(main) + ']'

    def get(self, index):
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

    def remove(self, index):
        current = self.head
        current_index = 0
        while current is not None:
            if index == 0:
                del_value = current.data
                self.head = current.next
                return del_value

            if current_index == index - 1:
                del_value = current.next.data
                current.next = current.next.next
                return del_value

            current = current.next
            current_index += 1

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

