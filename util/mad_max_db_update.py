from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

stack=[]
x=len(w.grid[0])//2
y=0
stack.append((w.grid[y][x],None,None))
while len(stack)>0:
  next_item=stack.pop()
  current_room=next_item[0]
  prev_direction=next_item[1]
  prev_room=next_item[2]
  new_room=Room(title=current_room.name, description=f'{current_room.description} No:{current_room.id}')
  new_room.save()
  if prev_room==None:
    first_room=new_room.id
  if current_room.n_to:
    if prev_direction !='n':
      stack.append((current_room.n_to,'s',new_room))
    else:
      new_room.connectRooms(prev_room,'n')
      prev_room.connectRooms(new_room,'s')
  if current_room.w_to:
    if prev_direction !='w':
      stack.append((current_room.w_to,'e',new_room))
    else:
      new_room.connectRooms(prev_room,'w')
      prev_room.connectRooms(new_room,'e')
  if current_room.e_to:
    if prev_direction !='e':
      stack.append((current_room.e_to,'w',new_room))
    else:
      new_room.connectRooms(prev_room,'e')
      prev_room.connectRooms(new_room,'w')
  if current_room.s_to:
    if prev_direction !='s':
      stack.append((current_room.s_to,'n',new_room))
    else:
      new_room.connectRooms(prev_room,'s')
      prev_room.connectRooms(new_room,'n')


players=Player.objects.all()
for p in players:
  p.currentRoom=first_room
  p.save()

