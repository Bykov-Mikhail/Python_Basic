class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def __iter__(self):
        return iter(self.stack)

    def put(self, elem, num = None):
        for item in self.stack:
            if item[0] == num:
                item.append(elem)
                return
        else:
            self.stack.append([num, elem])

        self.sorted()

    def get(self):
        if not self.stack:
            return None

        last_group = self.stack[-1]

        if len(self.stack) > 1:
            task = last_group.pop(1)

            if len(last_group) == 1:
                self.stack.pop()
            return task
        else:
            self.stack.pop()
            return None


    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def size(self):
        size = len(self.stack)
        return size

    def clear(self):
        self.stack.clear()

    def sorted(self):
        self.stack.sort(key=lambda x: x[0], reverse=True)

class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def __str__(self):
        lines = []
        for elem in self.stack:
            priority = elem[0]
            tasks = '; '.join(elem[1:])
            lines.append(f'{priority} - {tasks}')
        return '\n'.join(lines[::-1])


    def new_task(self, task, num_priority):
        self.stack.put(task, num_priority)

    def del_task(self):
        return self.stack.get()

manager = TaskManager()

manager.new_task("сделать уборку", 4)

manager.new_task("помыть посуду", 4)

manager.new_task("отдохнуть", 1)

manager.new_task("поесть", 2)

manager.new_task("сдать ДЗ", 2)

print(manager)

print('\n', manager.del_task())
print()

print(manager)

print('\n', manager.del_task())
print()

print(manager)