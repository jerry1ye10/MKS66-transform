from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.read().split("\n")
    f.close()
    #print('starting')
    i=0
    while i < len(lines):
        if lines[i] == "line":
            i += 1
            l = lines[i].split(' ')
            add_edge(points, int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]))
            i+=1
        elif lines[i] == "ident":
            i+=1
            ident(transform)
        elif lines[i] == "scale":
            i+=1
            l = lines[i].split(' ')
            matrix_mult(make_scale(int(l[0]), int(l[1]), int(l[2])), transform)
            i+=1
        elif lines[i] == "move":
            i+=1
            l = lines[i].split(' ')
            matrix_mult(make_translate(int(l[0]), int(l[1]), int(l[2])), transform)
            i+=1
        elif lines[i] == "rotate":
            i +=1
            l = lines[i].split(' ')
            l[1] = int(l[1])
            if l[0] == 'x':
                matrix_mult(make_rotX(l[1]), transform)
            elif l[0] == 'y':
                matrix_mult(make_rotY(l[1]), transform)
            else:
                matrix_mult(make_rotZ(l[1]), transform)
            i+=1
        elif lines[i] == "apply":
            matrix_mult(transform, points)
            i+=1
        elif lines[i] == "display":
            for r in range(len(points)):
				for c in range(len(points[0])):
					points[r][c] = int(points[r][c])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            i+=1
        elif lines[i] == "save":
            i+=1
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, lines[i].strip())
            print('done')
            i+=1
        else:
            break
