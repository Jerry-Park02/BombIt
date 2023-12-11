from characters import Army
from polygon import Polygon


class Level():
    def __init__(self, armys, columns, beams, wood, space):
        self.armys = armys
        self.columns = columns
        self.beams = beams
        self.woods = wood
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 20000
        self.two_star = 30000
        self.three_star = 40000
        self.bool_space = False
    
    def open_flat(self, x, y, n):
        """Create a open flat struture"""
        y0 = y
        for i in range(n):
            y = y0+90+i*90
            p = (x, y)
            self.columns.append(Polygon(p, 30, 60, self.space))
            p = (x+90, y)
            self.columns.append(Polygon(p, 30, 60, self.space))
            p = (x+45, y+45)
            self.beams.append(Polygon(p, 120, 30, self.space))

    def closed_flat(self, x, y, n):
        """Create a closed flat struture"""
        y0 = y
        for i in range(n):
            y = y0+100+i*125
            p = (x+1, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+60, y+22)
            self.columns.append(Polygon(p, 20, 85, self.space))
            p = (x+30, y+70)
            self.beams.append(Polygon(p, 85, 20, self.space))
            p = (x+30, y-30)
            self.beams.append(Polygon(p, 85, 20, self.space))

    def horizontal_pile(self, x, y, n):
        """Create a horizontal pile"""
        y += 80
        for i in range(n):
            p = (x + i * 30, y)
            self.columns.append(Polygon(p, 30, 60, self.space))

    def vertical_pile(self, x, y, n):
        """Create a vertical pile"""
        y += 30
        for i in range(n):
            p = (x, y+60+i*60)
            self.columns.append(Polygon(p, 30, 60, self.space))
    
    def wood_stack(self, x, y, n):
        """Create a vertical pile"""
        y += 40
        for i in range(n):
            p = (x, y+40+i*40)
            self.woods.append(Polygon(p, 40, 40, self.space))

    def build_0(self):
        """level 0"""
        army = Army(900, 80, self.space)
        self.armys.append(army)

        self.wood_stack(700, 0, 1)
        self.wood_stack(740, 0, 3)
        self.wood_stack(780, 0, 5)
        self.wood_stack(820, 0, 3)
        self.wood_stack(860, 0, 1)

        self.open_flat(950, 0, 1)

        army2 = Army(990, 70, self.space)
        self.armys.append(army2)

        self.number_of_birds = 4


    def build_1(self):
        """level 1"""
        army1 = Army(980, 100, self.space)
        army2 = Army(840, 100, self.space)
        self.armys.append(army1)
        self.armys.append(army2)
        
        p = (800, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))

        p = (900, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))

        p = (990, 90)
        self.columns.append(Polygon(p, 30,60, self.space))
        # beam below
        p = (850, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))

        p = (945, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))

        self.number_of_birds = 4



    def build_2(self):
        """level 2"""

        army = Army(978, 100, self.space)
        army.life = 30
        self.armys.append(army)
        army = Army(978, 200, self.space)
        army.life = 30

        self.armys.append(army)

        self.open_flat(950, 0, 3)
        self.horizontal_pile(950,300,4)

        self.wood_stack(720, 0, 1)
        self.wood_stack(760, 0, 3)
        self.wood_stack(800, 0, 5)
        self.wood_stack(840, 0, 3)
        self.wood_stack(880, 0, 1)

        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_3(self):
        """level 3"""
        army = Army(960, 100, self.space)
        army.life = 25
        self.armys.append(army)
        army = Army(885, 225, self.space)
        army.life = 25
        self.armys.append(army)
        army = Army(1070, 230, self.space)
        army.life = 25
        self.armys.append(army)

        p = (1160, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))
        p = (980, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))
        p = (800, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))
        
        p = (1070, 165)
        self.beams.append(Polygon(p, 120, 30, self.space))
        p = (890, 165)
        self.beams.append(Polygon(p, 120, 30, self.space))

        p = (890, 255)
        self.beams.append(Polygon(p, 120, 30, self.space))
        p = (1070, 255)
        self.beams.append(Polygon(p, 120, 30, self.space))

        p = (980, 285)
        self.beams.append(Polygon(p, 120, 30, self.space))
        p = (980, 375)
        self.beams.append(Polygon(p, 120,30, self.space))
        

        p = (755, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (845, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (935, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1025, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1115, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1205, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))

        p = (845, 210)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (935, 210)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1025, 210)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1115, 210)
        self.columns.append(Polygon(p, 30, 60, self.space))

        p = (935, 330)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1025, 330)
        self.columns.append(Polygon(p, 30, 60, self.space))

        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_4(self):
        """level 4"""

        p = (935, 270)
        self.beams.append(Polygon(p, 120, 30, self.space))
        self.vertical_pile(920, 0, 3)
        self.vertical_pile(950, 0, 3)
        army2 = Army(1000, 90, self.space)
        self.armys.append(army2)
        p = (1035, 270)
        self.beams.append(Polygon(p, 120, 30, self.space))
        self.vertical_pile(1020, 0, 3)
        self.vertical_pile(1050, 0, 3)
        army = Army(1100, 90, self.space)
        self.armys.append(army)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_5(self):
        """level 5"""
        army = Army(780, 70, self.space)
        self.armys.append(army)

        army = Army(1120, 70, self.space)
        self.armys.append(army)
     

        self.vertical_pile(600, 0, 1)
        self.vertical_pile(630, 0, 3)
        self.vertical_pile(660, 0, 5)
        self.vertical_pile(690, 0, 3)
        self.vertical_pile(720, 0, 1)

        self.wood_stack(840, 0, 1)
        self.wood_stack(880, 0, 3)
        self.wood_stack(920, 0, 5)
        self.wood_stack(960, 0, 3)
        self.wood_stack(1000, 0, 1)
        
        p = (1080, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1170, 90)
        self.columns.append(Polygon(p, 30, 60, self.space))
        p = (1125, 135)
        self.beams.append(Polygon(p, 120, 30, self.space))

        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def load_level(self):
        try:
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
