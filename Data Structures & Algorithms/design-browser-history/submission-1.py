class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.browsing_list = ListNode(homepage) # DummyNode

    def visit(self, url: str) -> None:
        # curr_tab = self.browsing_list
        new_tab = ListNode(url, None, self.browsing_list) # next is none, prev is none
        self.browsing_list.next = new_tab # current_website will point to new website
        self.browsing_list = new_tab # at current new website

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.browsing_list.prev or self.browsing_list.prev.val == -1:
                return self.browsing_list.val
            self.browsing_list = self.browsing_list.prev
        return self.browsing_list.val 

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.browsing_list.next:
                return self.browsing_list.val
            self.browsing_list = self.browsing_list.next
        return self.browsing_list.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)