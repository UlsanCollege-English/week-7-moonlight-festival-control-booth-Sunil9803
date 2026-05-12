[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-HC-VniT)

# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This homework uses Python’s heapq module to manage festival alerts based on priority. Each alert has a number where smaller values mean more urgent. The program processes alerts in the correct order, handles ties, and can return the top K alerts. It also includes a function to check the next alert without changing the original list.

---

## Approach

### order_festival_alerts

* I used a min heap (heapq) to store alerts.
* Each heap item was a tuple like (priority, title).
* I pushed all alerts into the heap, then popped them one by one.
* As I popped items, I added only the title to the result list.

---

### order_festival_alerts_stable

* I handled ties by adding an index to each item.
* Each heap item looked like (priority, index, title).
* If two priorities are the same, the index keeps the original order.
* Input order matters because we want earlier alerts first when priorities match.

---

### top_k_festival_alerts

* I used a heap and only removed the first k elements.
* This gives the most urgent alerts.
* If k <= 0, I returned an empty list.
* If k is larger than the list, I returned all alerts.

---

### peek_next_festival_alert

* I made a copy of the original list so it is not changed.
* Then I used heapify() to turn it into a heap.
* I returned the first element without popping it.
* If the list is empty, I returned None.

---

## Complexity

### order_festival_alerts

* *Time:* O(n log n)
* *Space:* O(n)
* *Why:* inserting and removing from heap takes log n time and we do it n times.

---

### order_festival_alerts_stable

* *Time:* O(n log n)
* *Space:* O(n)
* *Why:* same as above, but with an extra index stored.

---

### top_k_festival_alerts

* *Time:* O(n log n)
* *Space:* O(n)
* *Why:* building the heap takes O(n), removing k items takes O(k log n).

---

### peek_next_festival_alert

* *Time:* O(n)
* *Space:* O(n)
* *Why:* copying the list and heapifying both take linear time.

---

## Edge-case checklist

### order_festival_alerts

* [x] empty input
* [x] one alert
* [x] multiple different priorities

### order_festival_alerts_stable

* [x] same-priority tie
* [x] all same priority
* [x] empty input

### top_k_festival_alerts

* [x] k = 0
* [x] k > len(alerts)
* [x] duplicate priorities
* [x] empty input

### peek_next_festival_alert

* [x] empty input
* [x] normal case

---

## Test notes

* I tested normal and edge cases using pytest.
* I checked that heap order works correctly.
* I made sure original input is not modified in peek function.

---

## Assistance & Sources

### AI used?

* [x] Yes

If yes, what did it help with?

* Helped explain heap usage and structure the code clearly.
* Helped verify edge cases and test coverage.

### Other sources

* Python documentation for heapq
* Class notes

---

## Reflection

What was hardest?

* Understanding how to keep order when priorities are the same.

What do you understand better now?

* How heaps work and how to use them as a priority queue.
* How to handle edge cases properly.