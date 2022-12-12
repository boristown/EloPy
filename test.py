from elopy import *

i = Implementation(base_rating=1000)

i.addPlayer("Hank")
i.addPlayer("Boris")
i.addPlayer("Bill",rating=1200)

print(i.getPlayerRating("Hank"), i.getPlayerRating("Boris"), i.getPlayerRating("Bill"))

i.recordMatch("Hank","Bill",winner="Hank")
i.recordMatch("Hank","Boris",winner="Boris")

print(i.getRatingList())

i.recordMatch("Hank","Bill",winner="Bill")
i.recordMatch("Hank","Bill",winner="Bill")

print(i.getRatingList())

i.recordMatch("Hank","Bill",draw=True)
i.recordMatch("Hank","Boris",winner="Boris")

print(i.getRatingList())

i.removePlayer("Hank")

print(i.getRatingList())
