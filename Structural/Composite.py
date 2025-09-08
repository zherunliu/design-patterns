from abc import ABC
from typing import List


# component
class Component(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def display(self, depth: int) -> None:
        raise NotImplementedError("Subclasses must implement display method")

    def add(self, component: "Component") -> None:
        raise NotImplementedError("Unsupported operation: add")

    def remove(self, component: "Component") -> None:
        raise NotImplementedError("Unsupported operation: remove")


# composite
class Department(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children: List[Component] = []

    def add(self, component: Component):
        self.children.append(component)

    def display(self, depth: int):
        indent = "  " * depth
        print(f"{indent}{self.name}")

        for child in self.children:
            child.display(depth + 1)


# leaf
class Employee(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def display(self, depth: int) -> None:
        indent = "  " * depth
        print(f"{indent}{self.name}")


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.root = Department(name)

    def get_root(self):
        return self.root

    def display(self):
        print("Company Structure:")
        print(self.root.get_name())
        for child in self.root.children:
            child.display(1)


def count_leading_spaces(s: str):
    count = 0
    for char in s:
        if char == " ":
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    company_name = input().strip()
    company = Company(company_name)

    n = int(input())

    department_stack = [company.get_root()]

    for _ in range(n):
        line = input().rstrip()

        current_depth = count_leading_spaces(line)
        valid_content = line[current_depth:]

        current_level = current_depth // 2

        item_type, item_name = valid_content.split()

        if current_depth == 0:
            if item_type == "D":
                department = Department(item_name)
                company.get_root().add(department)

                department_stack.clear()
                department_stack.append(company.get_root())
                department_stack.append(department)
            elif item_type == "E":
                employee = Employee(item_name)
                department_stack[-1].add(employee)
        else:
            if item_type == "D":
                while current_level < len(department_stack) - 1:
                    department_stack.pop().name
                department = Department(item_name)
                department_stack[-1].add(department)
                department_stack.append(department)
            elif item_type == "E":
                employee = Employee(item_name)
                department_stack[-1].add(employee)

    company.display()
