# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN
# Authors: Jordan Kotler
# Last updated: 6th December 2018
# ####################################################

import utils
import numpy as np


def Tetris(target, limit_tetris):
    
    #   create padded target by adding a buffer of threes all around
   
    pad_target = np.pad(target, [3,3], mode='constant', constant_values=3)
    pad_height = len(pad_target)
    pad_width = len(pad_target[0])
    solution = [[(0,0) for col in range(0, pad_width)] for row in range(0, pad_height)]
    moved_coords = []
    one_here = [] #coordinates of ones in pad
    

#   find the coordinates of where there are ones in the target
    for i in range (3, pad_height-3):
        for j in range(3, pad_width-3):
            if pad_target [i][j] == 1:
                one_here.append([i,j])
                
                 
                
    i = 0
    x = 0
#   add a value of one_here (coordinate e.g. (3,4) to the shape's coordinates in order to change the shape's location
    while x < len(one_here):
        for i in limit_tetris:
            if limit_tetris[i] >= 1: #if there is that piece in limit tetris continue
            
                shapecoords = utils.generate_shape(i)
                
                good_place1 = (0 + ((one_here[x][0]))),(0 + ((one_here[x][1])))
                l = pad_target[good_place1[0]][good_place1[1]]
                
                good_place2 = (shapecoords[1][0] + ((one_here[x][0]))),(shapecoords[1][1] + ((one_here[x][1])))
                #adds the coordinate of a block in a shape to where there is a one
                m = pad_target[good_place2[0]][good_place2[1]]
                
                if m == 1:
                # check if that block also fits in a shape
                    
                    good_place3 = (shapecoords[2][0] + ((one_here[x][0]))),(shapecoords[2][1] + ((one_here[x][1])))
                    n = pad_target[good_place3[0]][good_place3[1]]
                    
                    if n == 1:
                        good_place4 = (shapecoords[3][0] + ((one_here[x][0]))),(shapecoords[3][1] + ((one_here[x][1])))
                        o = pad_target[good_place4[0]][good_place4[1]]
                         
                
                        if o ==1 and l == 1:
                            
                            moved_coords.append(good_place1)
                            pad_target[good_place1[0]][good_place1[1]] = 2
                            #two means i've place a piece there instead of just making it empty
                                 
                            moved_coords.append(good_place2)
                            pad_target[good_place2[0]][good_place2[1]] = 2
                            
                            moved_coords.append(good_place3)
                            pad_target[good_place3[0]][good_place3[1]] = 2
                               
                            moved_coords.append(good_place4)
                            pad_target[good_place4[0]][good_place4[1]] = 2
                               
                            moved_coords.append(i)
                            del one_here[x] #faster to include this function for some reason
                            limit_tetris[i]-=1

                  
        x+=1      

        
    x = 0
    
    #optimising:
#    
    good_place1 = 0
    good_place2 = 0
    good_place3 = 0
    good_place4 = 0
    
    while x<len(one_here):
        for a in limit_tetris:
            if limit_tetris[a] >= 1:
                optimshapes = utils.generate_shape(a)
                
                good_place1 = (0 + ((one_here[x][0]))),(0 + ((one_here[x][1])))
                l = pad_target[good_place1[0]][good_place1[1]]
                
                good_place2 = (optimshapes[1][0] + ((one_here[x][0]))),(optimshapes[1][1] + ((one_here[x][1])))
                m = pad_target[good_place2[0]][good_place2[1]]
                
                good_place3 = (optimshapes[2][0] + ((one_here[x][0]))),(optimshapes[2][1] + ((one_here[x][1])))
                n = pad_target[good_place3[0]][good_place3[1]]
                    
                good_place4 = (optimshapes[3][0] + ((one_here[x][0]))),(optimshapes[3][1] + ((one_here[x][1])))
                o = pad_target[good_place4[0]][good_place4[1]]
                
                if (l == 1 and m == 1 and n == 1 and o == 1) or (l == 1 and m == 0 and n == 1 and o == 1) or (l == 1 and m == 1 and n == 1 and o == 0) or (l == 1 and m == 1 and n == 0 and o == 1):
                    
                    moved_coords.append(good_place1)
                    pad_target[good_place1[0]][good_place1[1]] = 2
                    #two means i've place a piece there instead of just making it empty
                                 
                    moved_coords.append(good_place2)
                    pad_target[good_place2[0]][good_place2[1]] = 2
                    
                    moved_coords.append(good_place3)
                    pad_target[good_place3[0]][good_place3[1]] = 2
                               
                    moved_coords.append(good_place4)
                    pad_target[good_place4[0]][good_place4[1]] = 2
                    
                    moved_coords.append(a)
                    del one_here[x] #faster to include this function for some reason
                    limit_tetris[a]-=1
                  
        x+=1      

        
    x = 0
    
        
    moved_coords = [moved_coords[i:i+5] for i in range(0, len(moved_coords), 5)]
    #splits moved coords up into a list of lists, where moved_coords[i] is a list of 4 coordinates and a piece id value
    
#   change the (0,0) in solution to place a random piece in piece_idfor j in (0, len(piece_id)):      
    for i in range(0, len(moved_coords)):
        for j in range(0, 4): 
            solution[moved_coords[i][j][0]][moved_coords[i][j][1]] = (moved_coords[i][4], i+1)

          
    shrunken_solution = solution[3:-3]
    shrunken_solution = [i[3:-3] for i in shrunken_solution]            

    return shrunken_solution



