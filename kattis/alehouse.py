# https://open.kattis.com/problems/alehouse

n, k = map(int, input().split())

# Create events list
events = []
for _ in range(n):
    start, end = map(int, input().split())
    # For each interval, create an entry and exit event
    events.append((start, 1))     # 1 for entry
    events.append((end + 1, -1))  # -1 for exit (add 1 to include meeting at exit time)

# Sort events by time
events.sort()

current = 0  # current number of people
max_friends = 0  # maximum number of friends possible
start_idx = 0  # start of our window

# Process events in order
for i in range(len(events)):
    time, change = events[i]
    
    # Remove people that are now outside our k-window
    while start_idx < i and events[start_idx][0] <= time - k:
        current -= events[start_idx][1]
        start_idx += 1
    
    # Add current change
    current += change
    max_friends = max(max_friends, current)

print(max_friends)
    
