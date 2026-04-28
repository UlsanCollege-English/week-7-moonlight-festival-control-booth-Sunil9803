from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    Smaller priority numbers should be handled first.
    """
    heap = alerts[:]  # copy
    heapq.heapify(heap)

    result: list[str] = []
    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    If two alerts have the same priority, keep the original input order.
    """
    heap = [(priority, i, title) for i, (priority, title) in enumerate(alerts)]
    heapq.heapify(heap)

    result: list[str] = []
    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    """
    Return the titles of the k most urgent alerts.

    Stable for equal priorities.
    """
    if k <= 0 or not alerts:
        return []

    # Make it stable using index
    heap = [(priority, i, title) for i, (priority, title) in enumerate(alerts)]
    heapq.heapify(heap)

    result: list[str] = []
    for _ in range(min(k, len(heap))):
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    """
    Return the title of the next alert without modifying input.
    """
    if not alerts:
        return None

    heap = alerts[:]  # copy so original is unchanged
    heapq.heapify(heap)

    return heap[0][1]