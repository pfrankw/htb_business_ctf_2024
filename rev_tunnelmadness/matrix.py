import struct

def gen_row():
    return [0 for i in range(0, 20)]

def gen_layer():
    return [gen_row() for i in range(0, 20)]

def gen_empty_maze():
    return [gen_layer() for i in range(0, 20)]

with open('maze.bin', 'rb') as file:
    buf = file.read()

    maze = gen_empty_maze()
    
    for i in range(0, len(buf), 16):
        cell = buf[i:i+16]
        x = struct.unpack('<I', cell[0:4])[0]
        y = struct.unpack('<I', cell[4:8])[0]
        z = struct.unpack('<I', cell[8:12])[0]
        content = struct.unpack('<I', cell[12:16])[0]

        maze[z][y][x] = content

    for i in range(0, len(maze)):
        print(f"Layer[{i}]:")
        for row in reversed(maze[i]):
            for content in (row):
                if content == 2:
                    print('[W]', end='')
                elif content == 1 or content == 0:
                    print('[.]', end='')
                elif content == 3:
                    print('[!]', end='')
                else:
                    print(content, end='')
            print("")


# u
# u
# u
# rfu
# ru
# rrfrrffu
# u
# fu
# rru
# fu
# ffrfu
# fu
# u
# u
# ffrru
# u
# u
# fu
# rfd
# ffu
# ffrrrrrfrr