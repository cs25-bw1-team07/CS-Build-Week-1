class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    def generate_rooms(self, size_x, size_y, num_rooms):
        random.seed('9Lambda1Thunder1D0me9')
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        # Start from bottom center (0,8)
        x = 8
        y = -1  # (this will become 0 on the first step)
        last_x=None
        last_y=4
        room_count = 0
        # # Start generating rooms to the North
        direction = 1  # 1: North, 2: West, 3: East, 4:South
        # # While there are rooms to be created...
        previous_room = None
        vertical=[1,4]
        horizontal=[2,3]
        def get_dirs(x,y):
            retval=[]
            if self.grid[y+1][x]==None:
                if y < len(self.grid) - 1:
                    retval.append(1)
            if self.grid[y][x-1]==None:
                if x > 0:
                    retval.append(2)
            if self.grid[y][x+1]==None:
                if x < len(self.grid[0])-1:
                    retval.append(3)
            if self.grid[y-1][x]==None:
                if y>0:
                    retval.append(4)
                return retval
        while room_count < num_rooms:
            print("ROOM COUNT",room_count)
            # Calculate the direction of the room to be created
            if room_count>0:
                available_dir=get_dirs(x,y)
                print("Avail",available_dir)
                new_direction=random.randint(1, 4)
                if available_dir==[]:
                    break
                else:
                    while new_direction not in available_dir:
                        if new_direction in horizontal:
                            new_direction=tuple(horizontal)[new_direction==horizontal[0]]
                        if new_direction in vertical:
                            new_direction=tuple(horizontal)[new_direction==horizontal[0]]
                # print("RAND",new_direction)
                if direction in vertical and new_direction in vertical:
                    pass
                elif  direction in horizontal and new_direction in horizontal:
                    pass
                else:
                    if direction in horizontal:
                        last_x=new_direction
                    else:
                        last_y=new_direction
                    direction=new_direction
                # print("New",direction,last_x,last_y)
            if direction == 1 and y < size_y - 1:
                room_direction = "n"
                y += 1
            elif direction == 2 and x > 0:
                room_direction = "w"
                x -= 1
            elif direction == 3 and x < size_x-1:
                room_direction = "e"
                x += 1
            elif direction == 4 and y > 0:
                room_direction = "s"
                y -= 1
            else:
                # Change direction
                room_direction = "n"
                y += 1
            # Create a room in the given direction
            room = Room(room_count, "A Generic Room",
                        "This is a generic room.", x, y)
            # Save the room in the World grid
            self.grid[y][x] = room
            # Connect the new room to the previous room
            print("ROOM",previous_room,room,room_direction)
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)
            previous_room = room
            # Update iteration variables
            room_count += 1
            # print("XY", x, y, room_count)
    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"
        # Print string
        print(str)
