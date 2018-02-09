def has_cycle(head):
    if head is None:
        return False

    p1 = head
    p2 = head.next

    while p1 != p2:
        if p2 is None or p2.next is None:
            return False

        p1 = p1.next
        p2 = p2.next.next

    return True
