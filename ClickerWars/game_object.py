from pico2d import*

F = 0
T = 1

class OBJECT:
    location1 = None

    monsters1 = None
    monsters2 = None
    monsters3 = None
    monsters4 = None
    monsters5 = None
    monsters6 = None
    monsters7 = None
    monsters8 = None
    monsters9 = None
    monsters10 = None
    monsters_boss = None

    monsters_hp_unfilled = None
    monsters_hp_filled = None

    here_map = None
    next_map = None
    arrow = None

    damage_state = None
    coin_state = None
    coin = None

    font = None

    MONSTERS_STAND, MONSTERS_ATTACK = 1, 2

    def __init__(self):
        self.location1 = load_image('location/location_1.jpg')
        self.monsters1 = load_image('monsters/monsters1.png')
        self.monsters2 = load_image('monsters/monsters3.png')
        self.monsters3 = load_image('monsters/monsters5.png')
        self.monsters4 = load_image('monsters/monsters7.png')
        self.monsters5 = load_image('monsters/monsters9.png')
        self.monsters6 = load_image('monsters/monsters11.png')
        self.monsters7 = load_image('monsters/monsters13.png')
        self.monsters8 = load_image('monsters/monsters15.png')
        self.monsters9 = load_image('monsters/monsters17.png')
        self.monsters10 = load_image('monsters/monsters19.png')
        self.monsters_boss = load_image('monsters/monsters49.png')

        self.monsters_hp_unfilled = load_image('title&menu/main6.png')
        self.monsters_hp_filled = load_image('title&menu/main6.png')

        self.here_map = load_image('title&menu/main6.png')
        self.next_map = load_image('title&menu/main6.png')
        self.arrow = load_image('title&menu/main6.png')

        self.damage_state = load_image('title&menu/main6.png')
        self.coin_state = load_image('title&menu/main6.png')
        self.coin = load_image('title&menu/main6.png')

        self.font = load_font('sound&font/my_font.ttf')

        self.stage = 1

        self.click = F
        self.my_damage = 100
        self.monsters_hp = 0
        self.monsters_count = 1
        self.monsters_timeAttack = 20

        self.eat_coin = 0
        self.skill_upgrade = 100

        self.frame = 1
        self.frame_delay = 0
        self.state = self.MONSTERS_STAND

    def draw(self):
        if self.stage == 1:
            self.location1.draw(240, 400)
            self.here_map.clip_draw(565, 510, 90, 75, 240, 700)
            self.next_map.clip_draw(940, 114, 90, 75, 330, 700)
        elif self.stage == 2:
            pass

        if self.monsters_count == 1:
            self.monsters1.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 2:
            self.monsters2.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 3:
            self.monsters3.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 4:
            self.monsters4.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 5:
            self.monsters5.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 6:
            self.monsters6.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 7:
            self.monsters7.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 8:
            self.monsters8.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 9:
            self.monsters9.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 10:
            self.monsters10.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)
        if self.monsters_count == 11:
            self.monsters_boss.clip_draw(330 * self.frame, 1024 - 340 * self.state, 300, 300, 240, 440)

        self.monsters_hp_unfilled.clip_draw(130, 784, 210, 20, 240, 250)
        self.monsters_hp_filled.clip_draw(130, 809, 210 - self.monsters_hp, 20, 240 - self.monsters_hp / 2, 250)

        self.arrow.clip_draw(755, 404, 35, 60, 245, 680)

        self.damage_state.clip_draw(455, 0, 485, 190, 240, 80)
        self.coin_state.clip_draw(0, 474, 340, 60, 240, 775)
        self.coin.clip_draw(342, 759, 40, 35, 140, 770)
        self.coin.clip_draw(342, 759, 40, 35, 120, 770)

    def update(self):
        if self.state == self.MONSTERS_STAND:
            if self.frame_delay < 200:
                self.frame = 1
            elif self.frame_delay < 400:
                self.frame = 2
            else: self.frame_delay = 0
            self.frame_delay += 1

        if self.monsters_count == 11:
            if self.monsters_timeAttack >= 0:
                self.monsters_timeAttack -= 0.003
            else:
                self.monsters_hp = 0
                self.monsters_count = 1
                self.monsters_timeAttack = 20

        self.handle_state[self.state](self)

    def handle_stand(self):
        if self.monsters_hp >= 210:
            self.frame = 0
            self.monsters_hp = 0
            self.monsters_count += 1
        elif self.click == T:
            self.monsters_hp += self.my_damage
            self.state = self.MONSTERS_ATTACK

    def handle_attack(self):
        self.frame = 1
        if self.click == F:
            self.state = self.MONSTERS_STAND

    handle_state = {
        MONSTERS_STAND : handle_stand,
        MONSTERS_ATTACK : handle_attack
    }

    def data(self):
        self.font.draw(390, 90, "%2d" %self.my_damage)
        self.font.draw(260, 766, "%2d" %self.eat_coin)
        self.font.draw(20, 20, "upgrade click damage : %2d" %self.skill_upgrade)
        if self.monsters_count < 11:
            self.font.draw(50, 710, "%2d / 10" %self.monsters_count)
        elif self.monsters_count == 11:
            self.font.draw(30, 630, "BOSS : %2d" %self.monsters_timeAttack)