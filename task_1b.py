'''
*****************************************************************************************
*
*               ===============================================
*                   Rapid Rescuer (RR) Theme (eYRC 2019-20)
*               ===============================================
*
*  This script is to implement Task 1B of Rapid Rescuer (RR) Theme (eYRC 2019-20).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''


# Team ID:          [ Team-ID ]
# Author List:      [ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         task_1b.py
# Functions:        connect_to_server, send_to_receive_from_server, find_new_path
#                   [ Comma separated list of functions in this file ]
# Global variables: SERVER_IP, SERVER_PORT, SERVER_ADDRESS
#                   [ List of global variables defined in this file ]


# Import necessary modules
# Do not import any other modules
import cv2
import socket
import sys
import os
from datetime import datetime

# IP address of server (for now, loopback address)
SERVER_IP = '127.0.0.1'

# Port number assigned to server
SERVER_PORT = 3333
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)


def connect_to_server(SERVER_ADDRESS):

    """
    Purpose:
    ---
    the function creates socket connection with server

    Input Arguments:
    ---
    `SERVER_ADDRESS` :  [ tuple ]
        port address of server

    Returns:
    ---
    `sock` :    [ object of socket class ]
        object of socket class for socket communication

    Example call:
    ---
    sock = connect_to_server(SERVER_ADDRESS)

    """

    sock = None
    
    #############  Add your Code here   ###############

    

    ###################################################

    return sock


def send_to_receive_from_server(sock, shortestPath):

    """
    Purpose:
    ---
    the function sends / receives data to / from server

    Input Arguments:
    ---
    `sock` :    [ object of socket class ]
        object of socket class for socket communication
    `shortestPath`  :   [ list ]
        list of coordinates of shortest path from initial_point to final_point

    Returns:
    ---
    `sent_data` :   [ string ]
        data sent from client to server in proper format
    `recv_data` :   [ string ]
        data sent from server to client in proper format

    Example call:
    ---
    sent_data, recv_data = send_to_receive_from_server(sock, shortestPath)

    """

    sent_data = ''
    recv_data = ''

    #############  Add your Code here   ###############

    

    ###################################################

    return sent_data, recv_data

##  Function that computes new shortest path from cell adjacent to obstacle to final_point
def find_new_path(recv_data, shortestPath):

    """
    Purpose:
    ---
    the function computes new shortest path from cell adjacent to obstacle to final_point

    Input Arguments:
    ---
    `recv_data` :   [ string ]
        data sent from server to client in proper format
    `shortestPath`  :   [ list ]
        list of coordinates of shortest path from initial_point to final_point

    Returns:
    ---
    `obstacle_coord` :  [ tuple ]
        position of dynamic obstacle in (x,y) coordinate
    `new_shortestPath` :    [ list ]
        list of coordinates of shortest path from new_initial_point to final_point
    `new_initial_point` :   [ tuple ]
        coordinate of cell adjacent to obstacle for the new shortest path
    `img` : [ numpy array ]

    Example call:
    ---
    obstacle_coord, new_shortestPath, new_initial_point, img = find_new_path(recv_data, shortestPath)

    """

    obstacle_coord = ()
    new_shortestPath = []
    new_initial_point = ()

    global img_file_path, final_point, no_cells_height, no_cells_width

    #############  Add your Code here   ###############
    def func(a,b):
                    
                    if a==int(height-CELL_SIZE/2-1) and b==int(width-CELL_SIZE/2-1):
                                
                                    copy()
                                    global q
                                    q=q+1
                                    s.pop()
                                    return
                            
                    else:
                    
                                    for i in range(1,6):
                                                    x=a
                                                    y=b
                                                    if i==1 and original_binary_img[x][y+int(CELL_SIZE/2)-1]!=0 and (x,y+CELL_SIZE) not in s: 
                                                                    y=y+CELL_SIZE
                                                                    s.append((x,y))
                                                                    func(x,y)
                                    
    
                                                    if i==2 and original_binary_img[x+int(CELL_SIZE/2)-1][y]!=0 and (x+CELL_SIZE,y) not in s:
                                                                    x=x+CELL_SIZE
                                                                    s.append((x,y))
                                                                    func(x,y)
    
                                                    if i==3 and original_binary_img[x][y-int(CELL_SIZE/2)-1]!=0 and (x,y-CELL_SIZE) not in s:
                                                                    y=y-CELL_SIZE
                                                                    s.append((x,y))
                                                                    func(x,y)
    
                                                    if i==4 and original_binary_img[x-int(CELL_SIZE/2)-1][y]!=0 and (x-CELL_SIZE,y) not in s:
                                                                    x=x-CELL_SIZE
                                                                    s.append((x,y))
                                                                    func(x,y)
                                                    if i==5:
                                    
                                                                    s.pop()
                                                                    return

    

    s=[]
    t=[]
    global q
    q=0
    x=int(recv_data[2])
    y=int(recv_data[4])
    obstacle_coord=(x,y)
    i=shortestPath.index(obstacle_coord)
    k=shortestPath[i+1]
    a,b=k
    a=int((2*a+1)/2)
    a=10*(a+1)-1
    b=int((2*b+1)/2)
    b=10*(b+1)-1
    while len(shortestPath)!=i+1:
            shortestPath.pop()
    x,y=shortestPath[i]
    y=int((2*y+1)/2)
    y=10*(y+1)-1
    x=int((2*x+1)/2)
    x=10*(x+1)-1
    for i in range(1,6):
                                            
            if i==1 and original_binary_img[x][y+int(CELL_SIZE/2)-1]!=0 and (x,y+CELL_SIZE)!=(a,b):
                                        y=y+CELL_SIZE
                                        s.append((x,y))
                                        func1(x,y)
                
            if i==2 and original_binary_img[x+int(CELL_SIZE/2)-1][y]!=0 and (x+CELL_SIZE,y)!=(a,b):
                                        x=x+CELL_SIZE
                                        s.append((x,y))
                                        func1(x,y)
            if i==3 and original_binary_img[x][y-int(CELL_SIZE/2)-1]!=0 and (x,y-CELL_SIZE)!=(a,b):
                                        y=y-CELL_SIZE
                                        s.append((x,y))
                                        func1(x,y)
            if i==4 and original_binary_img[x-int(CELL_SIZE/2)-1][y]!=0 and (x-CELL_SIZE,y)!=(a,b):
                                        x=x-CELL_SIZE
                                        s.append((x,y))
                                        func1(x,y)
            if i==5:
                
                                        shortestPath.pop()
                                        return
    def func1(a,b):
            if a==int(height-CELL_SIZE/2-1) and b==int(width-CELL_SIZE/2-1):            
                                        copy()
                                        global q
                                        q=q+1
                                        s.pop()
                                        return
                            
            else:
                                        
                
                
                                        for i in range(1,6):
                                                        x=a
                                                        y=b
                                                        if i==1 and original_binary_img[x][y+int(CELL_SIZE/2)-1]!=0 and (x,y+CELL_SIZE) not in s and (x,y+CELL_SIZE)!=(x,y):
                                                                        
                                                                        
                                                                        y=y+CELL_SIZE
                                                                        s.append((x,y))
                                                                        func(x,y)
                                
                                                        if i==2 and original_binary_img[x+int(CELL_SIZE/2)-1][y]!=0 and (x+CELL_SIZE,y) not in s and (x+CELL_SIZE,y)!=(x,y):
                                                                        x=x+CELL_SIZE
                                                                        s.append((x,y))
                                                                        func(x,y)
                                                        if i==3 and original_binary_img[x][y-int(CELL_SIZE/2)-1]!=0 and (x,y-CELL_SIZE) not in s  and(x,y-CELL_SIZE)!=(x,y):
                                                                        y=y-CELL_SIZE
                                                                        s.append((x,y))
                                                                        func(x,y)
                                                        if i==4 and original_binary_img[x-int(CELL_SIZE/2)-1][y]!=0 and (x-CELL_SIZE,y) not in s and (x-CELL_SIZE,y)!=(x,y):
                                                                        x=x-CELL_SIZE
                                                                        s.append((x,y))
                                                                        func(x,y)
                                                        if i==5:
                                                                        s.pop()
                                                                        return
    
    def copy():
                        
            global q
            p=q
            t.append([])
            for j in s:
                                        t[p].append(j)
    
    s=t[0]
    for i in t:
            if len(i)<=len(s):
                                        s=i
    x,y=s[0]
    x=int((x+1)/10)
    x=x-int((x+1)/2)
    y=int((y+1)/10)
    y=y-int((y+1)/2)
    new_initial_point=(x,y)
    for i in s:
            x,y=i
            x=int((x+1)/10)
            x=x-int((x+1)/2)
            y=int((y+1)/10)
            y=y-int((y+1)/2)
            shortestPath.append((x,y))
    
    new_shortestPath=shortestPath
    

    return obstacle_coord, new_shortestPath, new_initial_point, img


#############   You can add other helper functions here     #############



#########################################################################


# NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
# Inputs:           None
# Outputs:          None
# Purpose:          the function first takes 'maze00.jpg' as input and solves the maze by calling connect_to_server,
#                   find_new_path and send_to_receive_from_server functions, it then asks the user whether to repeat
#                   the same on all maze images present in 'task_1b_images' folder or not

if __name__ == '__main__':
    
    curr_dir_path = os.getcwd()
    img_dir_path = curr_dir_path + '/../task_1b_images/'                # path to directory of 'task_1c_images'

    file_num = 0
    img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'     # path to 'maze00.jpg' image file

    # Importing task_1a and image_enhancer script
    try:
        task_1a_dir_path = curr_dir_path + '/../../Task 1A/codes'
        sys.path.append(task_1a_dir_path)

        import task_1a
        import image_enhancer

    except Exception as e:
        print('\n[ERROR] task_1a.py or image_enhancer.pyc file is missing from Task 1A folder !\n')
        exit()
    
    # To log data received from server
    output_file_name = 'data_from_server.txt'

    # remove the previously generated output txt file if exists
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    
    try:
    
        print('\n============================================')
        print('\nFor maze0' + str(file_num) + '.jpg')
        
        # Create socket connection with server
        try:
            sock = connect_to_server(SERVER_ADDRESS)

            if sock == None:
                print('\n[ERROR] connect_to_server function is not returning socket object in expected format !\n')
                exit()
            
            else:
                print('\nConnecting to %s Port %s' %(SERVER_ADDRESS))
        
        except ConnectionRefusedError as connect_err:
            print('\n[ERROR] the robot-server.c file is not executing, start the server first !\n')
            exit()
        
        try:        
            original_binary_img = task_1a.readImage(img_file_path)
            height, width = original_binary_img.shape

        except AttributeError as attr_err:
            print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
            exit()
        
        no_cells_height = int(height/task_1a.CELL_SIZE)                 # number of cells in height of maze image
        no_cells_width = int(width/task_1a.CELL_SIZE)                   # number of cells in width of maze image
        initial_point = (0, 0)                                          # start point coordinates of maze
        final_point = ((no_cells_height-1),(no_cells_width-1))          # end point coordinates of maze

        try:
            shortestPath = task_1a.solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

            if len(shortestPath) > 2:
                img = image_enhancer.highlightPath(original_binary_img, initial_point, final_point, shortestPath)
                
            else:
                print('\n[ERROR] shortestPath returned by solveMaze function in task_1a.py is incomplete !\n')
                exit()
        
        except TypeError as type_err:
            print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
            exit()

        print('\nShortest Path = %s \n\nLength of Path = %d' % (shortestPath, len(shortestPath)))

        cv2.imshow('canvas0' + str(file_num) + '_original_path', img)
        cv2.waitKey(0)

        sent_data, recv_data = send_to_receive_from_server(sock, shortestPath)

        if (sent_data.count('#') == 2) and (recv_data.count('@') == 2):
            print('\nSending %d bytes of data to server = %s' %(len(sent_data), sent_data))
            print('\nReceived %d bytes of data from server = %s' %(len(recv_data), recv_data))

            output_file = open(output_file_name, 'w')
            output_file.write('maze0' + str(file_num) + '.jpg' + '\n')
            output_file.write(recv_data[:-1] + '\n')

        else:
            print('\n[ERROR] sent / received data to / from server is not in proper format !\n')
            exit()

        obstacle_count = 0
        obstacle_list = []
        obstacle_pos = 0

        while '$' not in recv_data:

            obstacle_count = obstacle_count + 1

            try:
                obstacle_coord, new_shortestPath, new_initial_point, img = find_new_path(recv_data, shortestPath)

                if len(new_shortestPath) > 2:
                    img = image_enhancer.highlightPath(img, new_initial_point, final_point, new_shortestPath)
                    
                    print('\nDynamic Obstacle found at = (%d,%d)' %(obstacle_coord[0], obstacle_coord[1]))
                    print('\n--------------------------------------------')
                    print('\nNew Shortest Path = %s \n\nLength of new Path = %d' % (new_shortestPath, len(new_shortestPath)))
                
                else:
                    print('\n[ERROR] shortestPath returned by solveMaze function in task_1a.py is incomplete !\n')
                    exit()
            
            except TypeError as type_err:
                print('\n[ERROR] find_new_path function is not returning new shortest path in maze image in expected format !\n')
                exit()

            except IndexError as idx_err:
                print('\n[ERROR] find_new_path function is not returning obstacle coordinates in expected format !\n')
                exit()

            cv2.imshow('canvas0' + str(file_num) + '_obstacle_' + str(obstacle_count), img)
            cv2.waitKey(0)

            shortestPath = new_shortestPath
            sent_data, recv_data = send_to_receive_from_server(sock, shortestPath)

            if (sent_data.count('#') == 2) and (recv_data.count('@') == 2):
                print('\nSending %d bytes of data to server = %s' %(len(sent_data), sent_data))
                print('\nReceived %d bytes of data from server = %s' %(len(recv_data), recv_data))
                output_file.write(recv_data[:-1] + '\n')

            else:
                print('\n[ERROR] sent / received data to / from server is not in proper format !\n')
                exit()
        
        if (obstacle_count == 0):   print('\nNo Dynamic Obstacle for the image')
        
        else:   print('\nNo more Dynamic Obstacle for the image')

        print('\n============================================')
        
        cv2.imshow('canvas0' + str(file_num) + '_final_path', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        output_file.write(current_time + '\n')
        
        output_file.close()

        choice = input('\nWant to run your script on all maze images ? ==>> "y" or "n": ')

        if choice == 'y':

            if os.path.exists(output_file_name):

                os.remove(output_file_name)
            
            output_file = open(output_file_name, 'w')

            file_count = len(os.listdir(img_dir_path))

            for file_num in range(file_count):

                img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'     # path to 'maze00.jpg' image file

                print('\n============================================')
                print('\nFor maze0' + str(file_num) + '.jpg')
                
                try:        
                    original_binary_img = task_1a.readImage(img_file_path)
                    height, width = original_binary_img.shape

                except AttributeError as attr_err:
                    print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
                    exit()
                
                no_cells_height = int(height/task_1a.CELL_SIZE)                 # number of cells in height of maze image
                no_cells_width = int(width/task_1a.CELL_SIZE)                   # number of cells in width of maze image
                initial_point = (0, 0)                                          # start point coordinates of maze
                final_point = ((no_cells_height-1),(no_cells_width-1))          # end point coordinates of maze

                try:
                    shortestPath = task_1a.solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

                    if len(shortestPath) > 2:
                        img = image_enhancer.highlightPath(original_binary_img, initial_point, final_point, shortestPath)
                        
                    else:
                        print('\n[ERROR] shortestPath returned by solveMaze function in task_1a.py is incomplete !\n')
                        exit()
                
                except TypeError as type_err:
                    print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
                    exit()

                print('\nShortest Path = %s \n\nLength of Path = %d' % (shortestPath, len(shortestPath)))

                cv2.imshow('canvas0' + str(file_num) + '_original_path', img)
                cv2.waitKey(0)

                sent_data, recv_data = send_to_receive_from_server(sock, shortestPath)

                if (sent_data.count('#') == 2) and (recv_data.count('@') == 2):
                    print('\nSending %d bytes of data to server = %s' %(len(sent_data), sent_data))
                    print('\nReceived %d bytes of data from server = %s' %(len(recv_data), recv_data))

                    # output_file = open(output_file_name, 'w')
                    output_file.write('maze0' + str(file_num) + '.jpg' + '\n')
                    output_file.write(recv_data[:-1] + '\n')

                else:
                    print('\n[ERROR] sent / received data to / from server is not in proper format !\n')
                    exit()

                obstacle_count = 0
                obstacle_list = []
                obstacle_pos = 0

                while '$' not in recv_data:

                    obstacle_count = obstacle_count + 1

                    try:
                        obstacle_coord, new_shortestPath, new_initial_point, img = find_new_path(recv_data, shortestPath)

                        if len(new_shortestPath) > 2:
                            img = image_enhancer.highlightPath(img, new_initial_point, final_point, new_shortestPath)
                            
                            print('\nDynamic Obstacle found at = (%d,%d)' %(obstacle_coord[0], obstacle_coord[1]))
                            print('\n--------------------------------------------')
                            print('\nNew Shortest Path = %s \n\nLength of new Path = %d' % (new_shortestPath, len(new_shortestPath)))
                        
                        else:
                            print('\n[ERROR] shortestPath returned by solveMaze function in task_1a.py is incomplete !\n')
                            exit()
                    
                    except TypeError as type_err:
                        print('\n[ERROR] find_new_path function is not returning new shortest path in maze image in expected format !\n')
                        exit()

                    except IndexError as idx_err:
                        print('\n[ERROR] find_new_path function is not returning obstacle coordinates in expected format !\n')
                        exit()
                    
                    except Exception as e:
                        raise e

                    cv2.imshow('canvas0' + str(file_num) + '_obstacle_' + str(obstacle_count), img)
                    cv2.waitKey(0)

                    shortestPath = new_shortestPath
                    sent_data, recv_data = send_to_receive_from_server(sock, shortestPath)

                    if (sent_data.count('#') == 2) and (recv_data.count('@') == 2):
                        print('\nSending %d bytes of data to server = %s' %(len(sent_data), sent_data))
                        print('\nReceived %d bytes of data from server = %s' %(len(recv_data), recv_data))
                        output_file.write(recv_data[:-1] + '\n')

                    else:
                        print('\n[ERROR] sent / received data to / from server is not in proper format !\n')
                        exit()
                
                if (obstacle_count == 0):   print('\nNo Dynamic Obstacle for the image')
                
                else:   print('\nNo more Dynamic Obstacle for the image')

                print('\n============================================')
                
                cv2.imshow('canvas0' + str(file_num) + '_final_path', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            output_file.write(current_time + '\n')
            
            output_file.close()

            print('\nClosing Socket')
            sock.close()
        
        else:
            
            print('\nClosing Socket')
            sock.close()
    
    except KeyboardInterrupt:
        print('\nClosing Socket')
        sock.close()

