# LC: https://leetcode.com/problems/design-browser-history/

class DoublyLinkedNode:
    def __init__(self, v: str):
        self.val = v
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
      self.head = DoublyLinkedNode(homepage)

    def visit(self, url: str) -> None:
        new_node = DoublyLinkedNode(url)
        new_node.prev = self.head
        self.head.next = new_node
        self.head = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.head.prev:
                break

            self.head = self.head.prev
        
        return self.head.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.head.next:
                break

            self.head = self.head.next

        return self.head.val

