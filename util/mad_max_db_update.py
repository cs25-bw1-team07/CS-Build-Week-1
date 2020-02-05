from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

stack=[]
x=len(w.grid[0])//2
y=0
stack.append((w.grid[y][x],None,None))
while len(stack)>0:
  tup=stack.pop()
  curm=tup[0]
  prev=tup[1]
  prevrm=tup[2]
  # print("CURM",curm,prev)
  new_curm=Room(title=curm.name, description=f'{curm.description} No:{curm.id}')
  new_curm.save()
  if prevrm==None:
    first_room=new_curm.id
  if curm.n_to:
    if prev !='n':
      stack.append((curm.n_to,'s',new_curm))
    else:
      # print("Connect",curm.id,curm.n_to.id,'n')
      new_curm.connectRooms(prevrm,'n')
      prevrm.connectRooms(new_curm,'s')
  if curm.w_to:
    if prev !='w':
      stack.append((curm.w_to,'e',new_curm))
    else:
      # print("Connect",curm.id,curm.w_to.id,'w')
      new_curm.connectRooms(prevrm,'w')
      prevrm.connectRooms(new_curm,'e')
  if curm.e_to:
    if prev !='e':
      stack.append((curm.e_to,'w',new_curm))
    else:
      # print("Connect",curm.id,curm.e_to.id,'e')
      new_curm.connectRooms(prevrm,'e')
      prevrm.connectRooms(new_curm,'w')
  if curm.s_to:
    if prev !='s':
      stack.append((curm.s_to,'n',new_curm))
    else:
      # print("Connect",curm.id,curm.s_to.id,'s')
      new_curm.connectRooms(prevrm,'s')
      prevrm.connectRooms(new_curm,'n')


w.print_rooms()

players=Player.objects.all()
for p in players:
  p.currentRoom=first_room
  p.save()

