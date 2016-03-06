"""Return: the rectangle that is the intersection of a and b.
    If the intersection is invalid, return False instead.
    Check if input str or int.
"""
def intersection(a_x,a_y,a_width,a_height, b_x, b_y, b_width, b_height):
    #Getting the right and bottom edge of each
    right1 = int(a_x + a_width)
    bottom1 = int(a_y + a_height)
    right2 = int(b_x + b_width)
    bottom2 = int(b_y + b_height)
    
    #Finding edges of intersection
    left = int(max(a_x,b_x))
    right = int(min(right1, right2))
    top = int(max(a_y,b_y))
    bottom = int(min(bottom1, bottom2))
    
    #Computong width/height to make intersection
    width = right-left
    height = bottom - top
    
    if width < 0 or height < 0:
        print(False)
    else:
        print(True)

intersection('0', '0', '1', '1', '-1', '-1', '1', '1')