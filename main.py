import pygame

clock = pygame.time.Clock()

W = 1280  # variable de la taille de la fenêtre
H = 720

pygame.display.set_caption("Falling guy")  # création de la fenêtre
screen = pygame.display.set_mode((W, H))  # variable de la boucle du jeu

# image
arrow = pygame.image.load('assets/arrow.png').convert_alpha()
spike = pygame.image.load('assets/spike.png').convert_alpha()
bg = pygame.image.load('assets/bg2.png').convert()
tmp = []


class Game:
    def __init__(self):
        self.player = Player()
        self.spike = Spike()
        self.spike2 = Spike()
        self.spike3 = Spike()
        self.spike4 = Spike()
        self.arrow = Arrow()
        self.map = Map()
()

pygame.mixer.init()


class Map:
    def __init__(self):
        # all the different map
        self.tutorial_1 = [[12, 12, 12, 12, 12, 22, 22, 0, 0, 0, 0, 0, 22, 22, 12, 12, 12, 12, 12, 12],
                           [12, 12, 12, 12, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 12, 12, 12, 12],
                           [12, 12, 12, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 12, 12, 12],
                           [22, 22, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [2, 2, 2, 2, 2, 2, 2, 33, 34, 0, 0, 32, 2, 2, 2, 2, 2, 2, 2, 2],
                           [12, 12, 12, 12, 12, 12, 12, 0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 12, 12, 12]]

        self.easy_1 = [[12, 4, 23, 0, 21, 22, 6, 12, 12, 12, 12, 12, 12, 12, 22, 22, 22, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 55, 22, 6, 12, 15, 12, 12, 22, 0, 0, 0, 0, 0],
                       [22, 23, 0, 0, 0, 0, 55, 0, 38, 22, 22, 22, 6, 0, 0, 0, 0, 1, 2, 2],
                       [0, 0, 0, 0, 0, 0, 56, 0, 55, 0, 0, 0, 56, 0, 0, 0, 0, 11, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0, 0, 21, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 33, 33, 17, 12],
                       [3, 0, 0, 0, 0, 1, 43, 34, 0, 0, 1, 2, 43, 34, 0, 0, 0, 0, 0, 12],
                       [24, 2, 3, 0, 1, 26, 13, 0, 0, 0, 11, 12, 13, 0, 0, 0, 0, 0, 0, 12]]

        self.easy_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 12, 12, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 12, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 12, 12],
                       [2, 2, 3, 0, 0, 32, 2, 2, 2, 34, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22],
                       [12, 4, 23, 0, 0, 0, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 38, 12, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 55, 0, 11, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 55, 0, 11, 13, 0, 0, 54, 0, 0, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 56, 0, 11, 13, 0, 1, 52, 33, 34, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 0, 0, 11, 24, 2, 46, 0, 0, 0, 0, 0, 0, 0, 0],
                       [12, 13, 0, 0, 0, 0, 0, 1, 26, 12, 12, 13, 0, 0, 0, 0, 1, 2, 2, 2],
                       [12, 13, 30, 30, 30, 30, 30, 11, 12, 12, 12, 13, 0, 0, 0, 0, 11, 12, 12, 12], ]

        self.hard_1 = [[12, 12, 22, 22, 22, 22, 22, 12, 12, 12, 12, 22, 22, 22, 22, 22, 22, 22, 12, 12],
                       [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 12],
                       [13, 0, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
                       [24, 2, 0, 0, 0, 0, 0, 2, 12, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 12],
                       [12, 12, 2, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 12],
                       [12, 12, 12, 2, 0, 0, 2, 2, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 12],
                       [13, 0, 0, 0, 0, 2, 12, 12, 12, 0, 0, 0, 0, 0, 54, 0, 0, 0, 0, 12],
                       [13, 0, 0, 2, 2, 0, 0, 12, 12, 0, 0, 0, 0, 0, 24, 2, 2, 2, 2, 12],
                       [24, 3, 0, 0, 0, 0, 0, 12, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 12],
                       [22, 53, 34, 0, 0, 0, 2, 12, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 12],
                       [0, 0, 0, 0, 2, 2, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 12, 12],
                       [2, 2, 2, 2, 12, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 12, 12, 12]]

        self.hard_2 = [[0, 0, 0, 0, 0, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 6, 12, 12, 12, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 22, 22, 6, 12],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 6],
                       [2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
                       [12, 24, 2, 43, 34, 0, 0, 32, 41, 2, 43, 34, 0, 0, 0, 0, 0, 0, 0, 11],
                       [18, 22, 22, 44, 0, 0, 0, 0, 21, 18, 23, 0, 0, 1, 3, 0, 0, 0, 0, 11],
                       [55, 0, 0, 56, 0, 0, 0, 0, 0, 56, 0, 0, 0, 21, 53, 33, 34, 0, 0, 11],
                       [56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 17],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 41, 2, 43, 34, 0],
                       [0, 1, 2, 3, 0, 0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 21, 22, 23, 0, 0],
                       [2, 26, 12, 24, 30, 30, 30, 26, 12, 12, 24, 2, 2, 2, 30, 30, 30, 30, 30, 30]]

        self.hard_3 = [[22, 22, 22, 22, 22, 6, 12, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 21, 12, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                       [0, 0, 0, 0, 0, 0, 12, 12, 24, 2, 30, 30, 30, 30, 30, 30, 2, 2, 26, 12],
                       [43, 34, 0, 0, 0, 0, 12, 4, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                       [13, 0, 0, 32, 33, 33, 17, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
                       [12, 0, 0, 0, 0, 0, 11, 13, 0, 2, 2, 2, 3, 0, 1, 2, 2, 3, 0, 11],
                       [27, 33, 33, 34, 0, 0, 11, 13, 0, 0, 0, 0, 24, 2, 26, 0, 0, 13, 0, 11],
                       [13, 0, 0, 0, 0, 0, 12, 24, 2, 2, 3, 0, 0, 11, 0, 0, 0, 0, 0, 11],
                       [13, 0, 0, 32, 33, 33, 17, 0, 0, 4, 53, 34, 0, 37, 34, 0, 32, 33, 33, 26],
                       [12, 0, 0, 0, 0, 0, 21, 33, 33, 23, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0],
                       [12, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 12, 2, 0, 0, 0, 0, 0],
                       [12, 12, 24, 2, 2, 2, 2, 2, 2, 2, 2, 26, 12, 12, 12, 2, 2, 2, 2, 2]]

        self.hard_4 = [[12, 12, 12, 12, 12, 12, 4, 22, 18, 22, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                       [22, 18, 22, 12, 4, 22, 23, 0, 55, 0, 38, 22, 18, 22, 18, 22, 22, 6, 12, 12],
                       [0, 55, 0, 22, 44, 0, 0, 0, 55, 0, 55, 0, 55, 0, 55, 0, 0, 21, 18, 22],
                       [0, 56, 0, 0, 55, 0, 0, 0, 55, 0, 55, 0, 55, 0, 55, 0, 0, 0, 55, 0],
                       [0, 0, 0, 0, 55, 0, 0, 0, 55, 0, 56, 0, 55, 0, 56, 0, 0, 0, 55, 0],
                       [0, 0, 0, 0, 56, 0, 0, 0, 56, 0, 0, 0, 55, 0, 0, 0, 0, 0, 56, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 2, 2, 3, 0, 0, 0, 2, 2, 3, 0, 0, 0, 0, 0, 1, 2],
                       [0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 1, 2, 26, 12],
                       [2, 2, 30, 30, 12, 12, 30, 30, 30, 30, 30, 12, 30, 30, 30, 2, 26, 12, 12, 12]]

        self.hard_5 = [[12, 12, 22, 22, 22, 22, 22, 12, 12, 12, 22, 22, 22, 22, 22, 22, 22, 22, 22, 6],
                       [4, 22, 0, 0, 0, 0, 0, 22, 22, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
                       [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 11],
                       [13, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 12, 12, 12, 2, 2, 3, 0, 0, 11],
                       [13, 0, 0, 31, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
                       [13, 31, 0, 0, 55, 0, 0, 0, 31, 0, 32, 41, 3, 0, 0, 0, 0, 0, 0, 11],
                       [13, 0, 0, 31, 55, 0, 31, 0, 0, 0, 0, 21, 29, 3, 0, 0, 54, 0, 0, 11],
                       [23, 31, 0, 0, 55, 0, 0, 31, 0, 31, 0, 0, 21, 53, 2, 2, 46, 0, 0, 11],
                       [0, 0, 0, 0, 55, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 2, 2, 26],
                       [0, 0, 0, 1, 46, 0, 0, 0, 31, 0, 0, 2, 2, 0, 0, 0, 0, 22, 22, 22],
                       [2, 2, 2, 26, 24, 2, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0],
                       [12, 12, 12, 12, 12, 12, 2, 2, 2, 2, 2, 12, 2, 2, 2, 2, 2, 2, 2, 2]]

        self.hard_6 = [[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 22, 22, 22],
                       [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 22, 22, 22, 22, 0, 0, 0],
                       [22, 22, 22, 12, 12, 12, 12, 12, 12, 22, 22, 22, 22, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 22, 22, 22, 22, 22, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 55, 0, 0, 0, 0],
                       [2, 2, 2, 0, 0, 0, 0, 54, 0, 0, 0, 0, 55, 0, 0, 55, 0, 0, 0, 0],
                       [12, 12, 0, 0, 0, 54, 0, 55, 0, 0, 54, 0, 55, 0, 54, 55, 0, 2, 2, 2],
                       [12, 12, 0, 0, 0, 55, 0, 55, 0, 0, 55, 0, 55, 0, 55, 55, 0, 0, 12, 12],
                       [12, 12, 0, 0, 0, 55, 0, 55, 0, 0, 55, 0, 55, 0, 55, 55, 0, 0, 12, 12],
                       [12, 12, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 12, 12]]
        # different tile images
        self.tile_1 = pygame.image.load("Tiles/Tile_01.png").convert_alpha()  #
        self.tile_2 = pygame.image.load("Tiles/Tile_02.png").convert_alpha()  #
        self.tile_3 = pygame.image.load("Tiles/Tile_03.png").convert_alpha()  #
        self.tile_4 = pygame.image.load("Tiles/Tile_04.png").convert_alpha()  #
        self.tile_6 = pygame.image.load("Tiles/Tile_06.png").convert_alpha()  #
        self.tile_7 = pygame.image.load("Tiles/Tile_07.png").convert_alpha()
        self.tile_8 = pygame.image.load("Tiles/Tile_08.png").convert_alpha()
        self.tile_9 = pygame.image.load("Tiles/Tile_09.png").convert_alpha()
        self.tile_10 = pygame.image.load("Tiles/Tile_10.png").convert_alpha()  #
        self.tile_11 = pygame.image.load("Tiles/Tile_11.png").convert_alpha()  #
        self.tile_12 = pygame.image.load("Tiles/Tile_12.png").convert_alpha()  #
        self.tile_13 = pygame.image.load("Tiles/Tile_13.png").convert_alpha()  #
        self.tile_15 = pygame.image.load("Tiles/Tile_15.png").convert_alpha()  #
        self.tile_17 = pygame.image.load("Tiles/Tile_17.png").convert_alpha()  #
        self.tile_18 = pygame.image.load("Tiles/Tile_18.png").convert_alpha()  #
        self.tile_19 = pygame.image.load("Tiles/Tile_19.png").convert_alpha()
        self.tile_20 = pygame.image.load("Tiles/Tile_20.png").convert_alpha()
        self.tile_21 = pygame.image.load("Tiles/Tile_21.png").convert_alpha()  #
        self.tile_22 = pygame.image.load("Tiles/Tile_22.png").convert_alpha()  #
        self.tile_23 = pygame.image.load("Tiles/Tile_23.png").convert_alpha()  #
        self.tile_24 = pygame.image.load("Tiles/Tile_24.png").convert_alpha()  #
        self.tile_26 = pygame.image.load("Tiles/Tile_26.png").convert_alpha()  #
        self.tile_27 = pygame.image.load("Tiles/Tile_27.png").convert_alpha()
        self.tile_28 = pygame.image.load("Tiles/Tile_28.png").convert_alpha()
        self.tile_29 = pygame.image.load("Tiles/Tile_29.png").convert_alpha()
        self.tile_30 = pygame.image.load("Tiles/Tile_30.png").convert_alpha()  #
        self.tile_31 = pygame.image.load("Tiles/Tile_31.png").convert_alpha()  #
        self.tile_32 = pygame.image.load("Tiles/Tile_32.png").convert_alpha()  #
        self.tile_33 = pygame.image.load("Tiles/Tile_33.png").convert_alpha()  #
        self.tile_34 = pygame.image.load("Tiles/Tile_34.png").convert_alpha()  #
        self.tile_37 = pygame.image.load("Tiles/Tile_37.png").convert_alpha()
        self.tile_38 = pygame.image.load("Tiles/Tile_38.png").convert_alpha()
        self.tile_41 = pygame.image.load("Tiles/Tile_41.png").convert_alpha()  #
        self.tile_43 = pygame.image.load("Tiles/Tile_43.png").convert_alpha()
        self.tile_44 = pygame.image.load("Tiles/Tile_44.png").convert_alpha()
        self.tile_46 = pygame.image.load("Tiles/Tile_46.png").convert_alpha()  #
        self.tile_52 = pygame.image.load("Tiles/Tile_52.png").convert_alpha()
        self.tile_53 = pygame.image.load("Tiles/Tile_53.png").convert_alpha()  #
        self.tile_55 = pygame.image.load("Tiles/Tile_55.png").convert_alpha()  #
        self.tile_54 = pygame.image.load("Tiles/Tile_54.png").convert_alpha()  #
        self.tile_56 = pygame.image.load("Tiles/Tile_56.png").convert_alpha()  #

    # draw the map
    def draw(self, mapName):
        tile_size = 64
        tile_list = []
        mapLayout = ""

        if mapName == "Tutorial_1":
            mapLayout = self.tutorial_1
        if mapName == "easy_1":
            mapLayout = self.easy_1
        if mapName == "easy_2":
            mapLayout = self.easy_2
        if mapName == "hard_1":
            mapLayout = self.hard_1
        if mapName == "hard_2":
            mapLayout = self.hard_2
        if mapName == "hard_3":
            mapLayout = self.hard_3
        if mapName == "hard_4":
            mapLayout = self.hard_4
        if mapName == "hard_5":
            mapLayout = self.hard_5
        if mapName == "hard_6":
            mapLayout = self.hard_6

        posY = -48
        for row in mapLayout:
            posX = 0
            for tile in row:
                if tile == 1:
                    pygame.Surface.blit(screen, self.tile_1, (posX, posY))
                    tile_list.append(self.tile_1.get_rect(topleft=(posX, posY)))
                elif tile == 2:
                    pygame.Surface.blit(screen, self.tile_2, (posX, posY))
                    tile_list.append(self.tile_2.get_rect(topleft=(posX, posY)))
                elif tile == 3:
                    pygame.Surface.blit(screen, self.tile_3, (posX, posY))
                    tile_list.append(self.tile_3.get_rect(topleft=(posX, posY)))
                elif tile == 4:
                    pygame.Surface.blit(screen, self.tile_4, (posX, posY))
                    tile_list.append(self.tile_4.get_rect(topleft=(posX, posY)))
                elif tile == 6:
                    pygame.Surface.blit(screen, self.tile_6, (posX, posY))
                    tile_list.append(self.tile_6.get_rect(topleft=(posX, posY)))
                elif tile == 11:
                    pygame.Surface.blit(screen, self.tile_11, (posX, posY))
                    tile_list.append(self.tile_11.get_rect(topleft=(posX, posY)))
                elif tile == 12:
                    pygame.Surface.blit(screen, self.tile_12, (posX, posY))
                    tile_list.append(self.tile_12.get_rect(topleft=(posX, posY)))
                elif tile == 13:
                    pygame.Surface.blit(screen, self.tile_13, (posX, posY))
                    tile_list.append(self.tile_13.get_rect(topleft=(posX, posY)))
                elif tile == 15:
                    pygame.Surface.blit(screen, self.tile_15, (posX, posY))
                    tile_list.append(self.tile_15.get_rect(topleft=(posX, posY)))
                elif tile == 17:
                    pygame.Surface.blit(screen, self.tile_17, (posX, posY))
                    tile_list.append(self.tile_17.get_rect(topleft=(posX, posY)))
                elif tile == 18:
                    pygame.Surface.blit(screen, self.tile_18, (posX, posY))
                    tile_list.append(self.tile_18.get_rect(topleft=(posX, posY)))
                elif tile == 21:
                    pygame.Surface.blit(screen, self.tile_21, (posX, posY))
                    tile_list.append(self.tile_21.get_rect(topleft=(posX, posY)))
                elif tile == 22:
                    pygame.Surface.blit(screen, self.tile_22, (posX, posY))
                    tile_list.append(self.tile_22.get_rect(topleft=(posX, posY)))
                elif tile == 23:
                    pygame.Surface.blit(screen, self.tile_23, (posX, posY))
                    tile_list.append(self.tile_23.get_rect(topleft=(posX, posY)))
                elif tile == 24:
                    pygame.Surface.blit(screen, self.tile_24, (posX, posY))
                    tile_list.append(self.tile_24.get_rect(topleft=(posX, posY)))
                elif tile == 26:
                    pygame.Surface.blit(screen, self.tile_26, (posX, posY))
                    tile_list.append(self.tile_26.get_rect(topleft=(posX, posY)))
                elif tile == 27:
                    pygame.Surface.blit(screen, self.tile_27, (posX, posY))
                    tile_list.append(self.tile_27.get_rect(topleft=(posX, posY)))
                elif tile == 29:
                    pygame.Surface.blit(screen, self.tile_29, (posX, posY))
                    tile_list.append(self.tile_29.get_rect(topleft=(posX, posY)))
                elif tile == 30:
                    pygame.Surface.blit(screen, self.tile_30, (posX, posY))
                elif tile == 31:
                    pygame.Surface.blit(screen, self.tile_31, (posX, posY))
                    tile_list.append(self.tile_31.get_rect(topleft=(posX, posY)))
                elif tile == 32:
                    pygame.Surface.blit(screen, self.tile_32, (posX, posY))
                    tile_list.append(self.tile_32.get_rect(topleft=(posX, posY)))
                elif tile == 33:
                    pygame.Surface.blit(screen, self.tile_33, (posX, posY))
                    tile_list.append(self.tile_33.get_rect(topleft=(posX, posY)))
                elif tile == 34:
                    pygame.Surface.blit(screen, self.tile_34, (posX, posY))
                    tile_list.append(self.tile_34.get_rect(topleft=(posX, posY)))
                elif tile == 38:
                    pygame.Surface.blit(screen, self.tile_38, (posX, posY))
                    tile_list.append(self.tile_38.get_rect(topleft=(posX, posY)))
                elif tile == 37:
                    pygame.Surface.blit(screen, self.tile_37, (posX, posY))
                    tile_list.append(self.tile_37.get_rect(topleft=(posX, posY)))
                elif tile == 41:
                    pygame.Surface.blit(screen, self.tile_41, (posX, posY))
                    tile_list.append(self.tile_41.get_rect(topleft=(posX, posY)))
                elif tile == 43:
                    pygame.Surface.blit(screen, self.tile_43, (posX, posY))
                    tile_list.append(self.tile_43.get_rect(topleft=(posX, posY)))
                elif tile == 44:
                    pygame.Surface.blit(screen, self.tile_44, (posX, posY))
                    tile_list.append(self.tile_44.get_rect(topleft=(posX, posY)))
                elif tile == 46:
                    pygame.Surface.blit(screen, self.tile_46, (posX, posY))
                    tile_list.append(self.tile_46.get_rect(topleft=(posX, posY)))
                elif tile == 52:
                    pygame.Surface.blit(screen, self.tile_52, (posX, posY))
                    tile_list.append(self.tile_52.get_rect(topleft=(posX, posY)))
                elif tile == 53:
                    pygame.Surface.blit(screen, self.tile_53, (posX, posY))
                    tile_list.append(self.tile_53.get_rect(topleft=(posX, posY)))
                elif tile == 54:
                    pygame.Surface.blit(screen, self.tile_54, (posX, posY))
                    tile_list.append(self.tile_54.get_rect(topleft=(posX, posY)))
                elif tile == 55:
                    pygame.Surface.blit(screen, self.tile_55, (posX, posY))
                    tile_list.append(self.tile_55.get_rect(topleft=(posX, posY)))
                elif tile == 56:
                    pygame.Surface.blit(screen, self.tile_56, (posX, posY))
                    tile_list.append(self.tile_56.get_rect(topleft=(posX, posY)))

                posX += tile_size
            posY += tile_size

        return tile_list


class Player(pygame.sprite.Sprite):  # création du joueur

    def __init__(self):
        super().__init__()
        # stats
        self.HP = 100
        self.MHP = 100
        self.SP = 8
        self.JUMP = 20
        self.STGH = 10
        # texture et animations
        self.img = pygame.image.load('assets/player.png')
        self.rect = self.img.get_rect()
        # position et mouvement
        self.rect.x = 10
        self.rect.y = 528
        self.vel_y = 0
        self.SPAWN_X = 10
        self.SPAWN_Y = 528
        self.wall_jump = False
        self.cant_jump = -1
        self.width = self.rect.width
        self.height = self.rect.height
        self.soundJump = pygame.mixer.Sound("assets/sound/jump1.wav")
        self.soundDeath = pygame.mixer.Sound("assets/sound/death.wav")

    def gravity(self, dy):
        self.vel_y += 1.75
        if self.vel_y > 15:
            self.vel_y = 15
        dy += self.vel_y
        return dy

    def move(self):
        # print(self.rect.x, self.rect.y)
        # print('-=-=-=-=-=-')
        dx = 0
        dy = 0
        # detection de touches
        key = pygame.key.get_pressed()
        try:
            tile_list = m.draw(maps[mapState])
        finally:
            win()

        # saut
        if key[pygame.K_SPACE] and self.cant_jump <= 0 or key[pygame.K_UP] and self.cant_jump <= 0:
            self.cant_jump += 1
            self.vel_y = -self.JUMP
            dy += self.vel_y

            self.soundJump.play()

        # déplacement gauche
        if key[pygame.K_LEFT] and self.rect.x > 0:
            dx -= self.SP

        # déplacement droite
        if key[pygame.K_RIGHT] and self.rect.x + self.rect.width < W:
            dx += self.SP

        # gravité
        if self.wall_jump is False:
            dy = self.gravity(dy)

        # collision
        for tile in tile_list:
            # collision x
            if tile.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # collision y
            if tile.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # au dessus ?

                if self.wall_jump and key[pygame.K_SPACE]:
                    dy -= self.JUMP
                    self.wall_jump = False

                elif self.wall_jump and key[pygame.K_SPACE]:
                    dy -= self.JUMP
                    self.wall_jump = False

                if self.vel_y < 0:
                    dy = tile.bottom - self.rect.top
                    self.vel_y = 0

                # en dessous ?
                elif self.vel_y >= 0:
                    dy = tile.top - self.rect.bottom
                    self.vel_y = 0
                    self.cant_jump = 0

        game.spike.loop()
        game.spike2.loop()
        game.spike3.loop()
        game.spike4.loop()
        game.arrow.loop()

        # update du déplacement du joueur
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.y > H - self.rect.height:
            self.rect.x = self.SPAWN_X
            self.rect.y = self.SPAWN_Y
            self.soundDeath.play()


class Spike:
    def __init__(self):
        global spike
        self.img = spike
        self.rect = self.img.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.pos = (self.rect.x, self.rect.y)
        self.width = self.rect.width
        self.height = self.rect.height

    def loop(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        if game.player.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            game.player.rect.x = game.player.SPAWN_X
            game.player.rect.y = game.player.SPAWN_Y
            game.player.soundDeath.play()


class Arrow:
    def __init__(self):
        global arrow
        self.SP = 7

        self.img = arrow
        self.soundShoot = pygame.mixer.Sound('assets/sound/arrow.wav')

        self.rect = self.img.get_rect()
        self.pos = (0, 0)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.width = self.rect.width
        self.height = self.rect.height

        self.range = arrow_range[0]
        self.start_X = self.rect.x
        self.end_X = self.rect.x + self.range

    def loop(self):
        self.rect.x += self.SP
        if self.rect.x > self.end_X:
            self.rect.x = self.start_X

        if game.player.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
            game.player.rect.x = game.player.SPAWN_X
            game.player.rect.y = game.player.SPAWN_Y
            game.player.soundDeath.play()

    def set_spawn(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.start_X = self.pos[0]
        self.range = arrow_range[mapState]
        self.end_X = self.rect.x + self.range
        self.SP = arrow_sp[mapState]
        self.soundShoot.play()


def flag_anim():
    global flags_frame, FLAGS_FRAMES
    if flags_frame >= 16:
        flags_frame = 0
    flags_frame += 1
    frame = int(flags_frame / 4) - 1
    return FLAGS_FRAMES[frame]


def mapChange():
    global mapState, maprect, run, maps
    flag = pygame.image.load(flag_anim())
    flagpos = (1152, 528)
    soundwin = pygame.mixer.Sound("assets/sound/win.wav")
    if mapState == 0:
        flagpos = (1152, 528)
        screen.blit(flag, flagpos)
    if mapState == 1:
        flagpos = (1024, 464)
        screen.blit(flag, flagpos)
    if mapState == 2:
        flagpos = (1189, 528)
        screen.blit(flag, flagpos)
    if mapState == 3:
        flagpos = (1157, 464)
        screen.blit(flag, flagpos)
    if mapState == 4:
        flagpos = (64, 80)
        screen.blit(flag, flagpos)
    if mapState == 5:
        flagpos = (1152, 592)
        screen.blit(flag, flagpos)
    if mapState == 6:
        flagpos = (1216, 464)
        screen.blit(flag, flagpos)
    if mapState == 7:
        flagpos = (1216, 592)
        screen.blit(flag, flagpos)
    if mapState == 8:
        flagpos = (1216, 400)
        screen.blit(flag, flagpos)

    if flag.get_rect(topleft=flagpos).colliderect(game.player.rect):
        mapState += 1
        soundwin.play()
        try:
            maprect = game.map.draw(maps[mapState])

            game.spike.pos = spike_position[mapState][0]
            game.spike2.pos = spike_position[mapState][1]
            game.spike3.pos = spike_position[mapState][2]
            game.spike4.pos = spike_position[mapState][3]
            game.arrow.pos = arrow_position[mapState][0]
            game.arrow.set_spawn()

            if mapState == 0:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 528
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 1:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 464
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 2:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 128
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 3:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 592
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 4:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 592
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 5:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 64
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 6:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 608
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 7:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 576
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
            elif mapState == 8:
                game.player.vel_y = 0
                game.player.SPAWN_Y = 336
                game.player.rect.y = game.player.SPAWN_Y
                game.player.SPAWN_X = 10
                game.player.rect.x = game.player.SPAWN_X
        except:
            win()
            return

        return maprect


def win():
    global mapState, maps, run, finaleTime

    if mapState >= len(maps):
        run = False
        print("you win")
        print(finaleTime)

        return run




# Variables
spike_position = [
    [(-100, -100), (-100, -100), (-100, -100), (-100, -100)],  # 1
    [(256, 605), (-100, -100), (-100, -100), (-100, -100)],  # 2
    [(380, 90), (640, 484), (768, 364), (1100, 564)],  # 3
    [(708, 416), (64, 100), (1064, 364), (832, 632)],  # 4
    [(200, 151), (960, 280), (710, 600), (-100, -100)],  # 5
    [(320, 171), (320, 415), (180, 630), (832, 285)],  # 6
    [(960, 600), (-100, -100), (-100, -100), (-100, -100)],  # 7
    [(576, 358), (1088, 415), (1152, 415), (-100, -100)],  # 8
    [(320, 415), (896, 415), (-100, -100), (-100, -100)],  # 9

]

arrow_position = [
    [(-100, -100), (-100, -100)],  # 1
    [(-100, -100), (-100, -100)],  # 2
    [(512, 232), (-100, -100)],  # 3
    [(128, 256), (576, 320)],  # 4
    [(-100, -100), (-100, -100)],  # 5
    [(480, 258), (-100, -100)],  # 6
    [(-100, -100), (-100, -100)],  # 7
    [(710, 624), (-100, -100)],  # 8
    [(430, 415), (-100, -100)],  # 9

]
arrow_sp = [
    1,  # 1
    1,  # 2
    10,  # 3
    8,  # 4
    1,  # 5
    12,  # 6
    1,  # 7
    12,  # 8
    15,  # 9
]
arrow_range = [
    10,  # 1
    10,  # 2
    750,  # 3
    400,  # 4
    100,  # 5
    900,  # 6
    100,  # 7
    600,  # 8
    370,  # 9
]

mapState = 0
game = Game()
m = Map()
run = True
maps = ["Tutorial_1", "easy_1", "easy_2", "hard_1", "hard_2", "hard_3", "hard_4", "hard_5", "hard_6", ]
current = -1
FLAGS_FRAMES = ["assets/Flag.png", "assets/Flag1.png", "assets/Flag2.png", "assets/Flag3.png"]
flags_frame = 0
finaleTime = 0

pygame.init()  # initialisation de pygame

game.map.draw(maps[mapState])

while run:
    clock.tick(60)
    # ajout des images sur le screen
    finaleTime +=1
    screen.blit(bg, (0, 0))
    screen.blit(game.player.img, game.player.rect)
    screen.blit(game.spike.img, game.spike.rect)
    screen.blit(game.spike2.img, game.spike2.rect)
    screen.blit(game.spike3.img, game.spike3.rect)
    screen.blit(game.spike4.img, game.spike4.rect)
    screen.blit(arrow, game.arrow.rect)
    mapChange()
    win()
    if not run:
        break
    game.player.move()
    if not run:
        break

    pygame.display.flip()

    # teste des events
    for event in pygame.event.get():
        # joueur quitte ?
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
