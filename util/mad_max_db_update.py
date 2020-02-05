from django.contrib.auth.models import User
from adventure.models import Player

# Room.objects.all().delete()

# print(w.grid)
stack=[]
x=len(w.grid[0])//2
y=0
# print("XY",x,y)
stack.append((w.grid[y][x],None,None))
while len(stack)>0:
  tup=stack.pop()
  curm=tup[0]
  prev=tup[1]
  prevrm=tup[2]
  # print("CURM",curm,prev)
  # curm.save()
  if curm.n_to:
    if prev !='n':
      stack.append((curm.n_to,'s',curm))
    else:
      print("Connect",curm.id,curm.n_to.id,'n')
    # curm.connectRooms(curm.n_to,'n')
  if curm.w_to:
    if prev !='w':
      stack.append((curm.w_to,'e',curm))
    else:
      print("Connect",curm.id,curm.w_to.id,'w')
    # curm.connectRooms(curm.w_to,'w')
  if curm.e_to:
    if prev !='e':
      stack.append((curm.e_to,'w',curm))
    else:
      print("Connect",curm.id,curm.e_to.id,'e')
    # curm.connectRooms(curm.e_to,'e')
  if curm.s_to:
    if prev !='s':
      stack.append((curm.s_to,'n',curm))
    else:
      print("Connect",curm.id,curm.s_to.id,'s')
    # curm.connectRooms(curm.s_to,'s')
w.print_rooms()


# w.grid[3][3].n_to

# r_outside = Room(title="Outside Cave Eeentrance",
#                  description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()

# Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

# players=Player.objects.all()
# for p in players:
#   p.currentRoom=r_outside.id
#   p.save()



