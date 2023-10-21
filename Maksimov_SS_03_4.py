'''
You are a big fan of Formula 1.
There was a race last week-end, but ... you missed the live TV. 
You picked on the internet a list of the events during the race, and you want to get your champion's rank at the end of the race........
'''

def get_rank(champion_id, event_string):
    rank = champion_id
    events = event_string.split()

    for event in events:
        if event == "O":
            rank += 1
        elif event == "I":
            return -1

    return rank

# Example
event_string = "2 O 12 I"
champion_id = 2

rank = get_rank(champion_id, event_string)
print(rank) #Output: -1