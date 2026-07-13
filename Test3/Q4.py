'''4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced'''



timings = list(map(float, input("Enter race timings:").split()))
timings.sort()
print("Ranked Timings :", timings)
