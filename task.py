class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def get_size(self) -> int:
        return self._size


    def add_first(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def add_last(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1


    def remove_first(self):
        if self.is_empty():
            raise IndexError("Помилка: Список порожній")
        
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return removed_data

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Помилка: Список порожній")
        
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removed_data


    def contains(self, data) -> bool:
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def _get_node(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError(f"Помилка: Індекс {index} поза межами списку [0, {self._size - 1}]")
        
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1, index, -1):
                current = current.prev
        return current

    def get(self, index: int):
        return self._get_node(index).data


    def insert(self, index: int, data) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Помилка: Неприпустимий індекс {index}")
        
        if index == 0:
            self.add_first(data)
        elif index == self._size:
            self.add_last(data)
        else:
            target_node = self._get_node(index)
            new_node = Node(data)

            new_node.prev = target_node.prev
            new_node.next = target_node
            target_node.prev.next = new_node
            target_node.prev = new_node
            self._size += 1

    def remove_at(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError(f"Помилка: Індекс {index} поза межами списку")
        
        if index == 0:
            return self.remove_first()
        elif index == self._size - 1:
            return self.remove_last()
        else:
            target_node = self._get_node(index)
            target_node.prev.next = target_node.next
            target_node.next.prev = target_node.prev
            self._size -= 1
            return target_node.data

    def insert_range(self, index: int, elements: list) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Помилка: Неприпустимий індекс {index}")
        
        for i, val in enumerate(elements):
            self.insert(index + i, val)


    def get_max(self):
        if self.is_empty():
            raise ValueError("Помилка: Список порожній")
        
        max_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def get_min(self):
        if self.is_empty():
            raise ValueError("Помилка: Список порожній")
        
        min_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val


    def display(self) -> str:
        if self.is_empty():
            return "{}"
        
        items = []
        current = self.head
        index = 0
        while current is not None:
            items.append(f"[index:{index}; value:{current.data}]")
            current = current.next
            index += 1
            
        return "{" + " ".join(items) + "}"

    def __str__(self) -> str:
        return self.display()


if __name__ == "__main__":
    print("=== Практична робота №10: Двобічно зв'язний список ===")
    dll = DoublyLinkedList()

    print("\n--- 1. Додавання елементів (add_last, add_first) ---")
    dll.add_last(45)
    dll.add_first(10)
    dll.add_last(57)
    print(f"Список: {dll.display()}")
    print(f"Розмір: {dll.get_size()}")

    print("\n--- 2. Найбільший та найменший елементи ---")
    print(f"Найбільший: {dll.get_max()}")
    print(f"Найменший: {dll.get_min()}")

    print("\n--- 3. Перевірка contains та get ---")
    print(f"Елемент за індексом 1: {dll.get(1)}")
    print(f"Чи існує 45 у списку: {dll.contains(45)}")
    print(f"Чи існує 99 у списку: {dll.contains(99)}")

    print("\n--- 4. Операції за індексом (insert, remove_at) ---")
    dll.insert(1, 20)
    print(f"Після вставки 20 на індекс 1: {dll.display()}")
    
    removed = dll.remove_at(2)
    print(f"Видалено значення: {removed}")
    print(f"Список після remove_at(2): {dll.display()}")

    print("\n--- 5. Додавання множини елементів (insert_range) ---")
    dll.insert_range(1, [100, 200])
    print(f"Після додавання [100, 200] на індекс 1: {dll.display()}")

    print("\n--- 6. Видалення з країв (remove_first, remove_last) ---")
    print(f"Вилучено перший: {dll.remove_first()}")
    print(f"Вилучено останній: {dll.remove_last()}")
    print(f"Фінальний список: {dll.display()}")
    print(f"Фінальний розмір: {dll.get_size()}")