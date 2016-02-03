f = [line.split() for line in open('placeholder.txt')][1:]
d = {}

for _, room_number, direction, time in f:
    if not room_number in d:
        d[room_number] = []
    d[room_number].append(-int(time) if direction == 'I' else int(time))

sorted_d = sorted(d, key=lambda x: int(x))
for key in sorted_d:
    visitors = len(d[key]) / 2
    print("Room %2s, %d minute average visit, %d visitor(s) total" % 
          (key, sum(d[key])/visitors, visitors))



    ###The Input

# Each line in the text file represents either a visitor entering or leaving a room. It starts with an integer, representing a visitor's unique identifier. Next on this line is another integer, representing the room's number. Next is a single character, either 'I' (for "In") for this visitor entering the room, or 'O' (for "out") for the visitor leaving the room. Finally, at the end of this line, there is a time-stamp integer: it is an integer representing the minute the event occurred during the day. All of these elements are space-delimited.

# You may assume that all input is logically well-formed: for each person entering a room, he or she will always leave it at some point in the future. A visitor will only be in one room at a time.

# Note that the order of events in the log are not sorted in any way; it shouldn't matter, as you can solve this problem without sorting given data.

# Sample Input:

		#0 0 I 540
		# 1 0 I 540
		# 0 0 O 560
		# 1 0 O 560

###The Output

# For each room that had log data associated with it, print the room number, then print the average length of time visitors have stayed as an integer, and then finally print the total number of visitors in the room. All of this should be on the same line and be space delimited; you may optionally include labels on this text, like in our sample output 1.

# Sample Output:

# 		Room 0, 20 minute average visit, 2 visitor(s) total

