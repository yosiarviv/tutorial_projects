import socket
import pickle
from _thread import *
from game import Game
from player import Player
import sys


server = "192.168.1.40"
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print ("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p,gameId):
    global idCount


while True:
    conn, addr = s.accept()
    print ("Connected to: " , addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1 )//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p , gameId))
