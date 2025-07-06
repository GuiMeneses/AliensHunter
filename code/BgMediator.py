from code.BackGround import BackGround
from code.Const import WIN_HEIGHT


class BgMediator:
    def __init__(self, screen):
        self.list_bg_0: list[BackGround] = [BackGround('Background_1', (0, 0), screen),
                                            BackGround('Background_2', (0, 0), screen),
                                            BackGround('Background_3', (0, 0), screen),
                                            BackGround('Background_4', (0, 0), screen)]

        self.list_bg_1: list[BackGround] = [BackGround('Background_1', (0, WIN_HEIGHT), screen),
                                            BackGround('Background_2', (0, WIN_HEIGHT), screen),
                                            BackGround('Background_3', (0, WIN_HEIGHT), screen),
                                            BackGround('Background_4', (0, WIN_HEIGHT), screen)]

    def run(self):
        for i in range(4):
            self.list_bg_0[i].draw()
            self.list_bg_1[i].draw()

            self.list_bg_0[i].move(self.list_bg_1[i])
            self.list_bg_1[i].move(self.list_bg_0[i])
