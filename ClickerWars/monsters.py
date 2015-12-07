from pico2d import*

import random

image_size = 1024
false = 0
true = 1

class Monsters:
    image0 = None
    image1 = None
    image2 = None
    image3 = None
    image4 = None
    image5 = None
    image6 = None
    image7 = None
    image8 = None
    image9 = None
    boss = None

    unfilled_hp_state = None
    filled_hp_state   = None

    font = None

    MONSTERS_STAND, MONSTERS_ATTACK = 1, 2

    def __init__(self):
        self.image0 = load_image('monsters/monsters1.png')
        self.image1 = load_image('monsters/monsters3.png')
        self.image2 = load_image('monsters/monsters5.png')
        self.image3 = load_image('monsters/monsters7.png')
        self.image4 = load_image('monsters/monsters9.png')
        self.image5 = load_image('monsters/monsters11.png')
        self.image6 = load_image('monsters/monsters13.png')
        self.image7 = load_image('monsters/monsters15.png')
        self.image8 = load_image('monsters/monsters17.png')
        self.image9 = load_image('monsters/monsters19.png')
        self.boss = load_image('monsters/monsters49.png')

        self.unfilled_hp_state = load_image('title&menu/main6.png')
        self.filled_hp_state = load_image('title&menu/main6.png')

        self.font = load_font('sound&font/my_font.ttf')

        self.hp = 0
        self.boss_time = 20
        self.damage = 10
        self.click = false
        self.get_coin = 0
        self.upgrade_coin = 100
        self.monster_count = 1

        self.frame = 1
        self.frame_delay = 0
        self.state = self.MONSTERS_STAND

    def draw(self):
        if self.monster_count == 1:
            self.image0.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 2:
            self.image1.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 3:
            self.image2.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 4:
            self.image3.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 5:
            self.image4.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 6:
            self.image5.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 7:
            self.image6.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 8:
            self.image7.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 9:
            self.image8.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 10:
            self.image9.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)
        if self.monster_count == 11:
            self.boss.clip_draw(330 * self.frame, image_size - 340 * self.state, 300, 300, 240, 440)

        self.unfilled_hp_state.clip_draw(130, image_size - 240, 210, 20, 240, 250)
        self.filled_hp_state.clip_draw(130, image_size - 215, 210 - self.hp, 20, 240 - self.hp / 2, 250)

    def update(self):
        if self.state == self.MONSTERS_STAND:
            if self.frame_delay < 200:
                self.frame = 1
            elif self.frame_delay < 400:
                self.frame = 2
            else: self.frame_delay = 0
            self.frame_delay += 1
        if self.monster_count == 11:
            self.boss_time -= 0.003
        self.handle_state[self.state](self)

    def handle_stand(self):
        if self.hp >= 210:
            self.frame = 0
            self.hp = 0
            self.monster_count += 1
        elif self.click == true:
            self.hp += self.damage
            self.state = self.MONSTERS_ATTACK

    def handle_attack(self):
        self.frame = 1
        if self.click == false:
            self.state = self.MONSTERS_STAND

    handle_state = {
        MONSTERS_STAND:handle_stand,
        MONSTERS_ATTACK:handle_attack
    }

    def show_data(self):
        if self.monster_count < 11:
            self.font.draw(50, 710, "%2d / 10" %self.monster_count)
        self.font.draw(220, 766, "coin : %2d" %self.get_coin)
        self.font.draw(20, 130, "upgrade click 'a' : need coin %2d" %self.upgrade_coin)
        #self.font.draw(20, 130, "upgrade skill 's' : need coin %2d" %monsters.upgrade_coin)
        #self.font.draw(20, 130, "upgrade skill 'd' : need coin %2d" %monsters.upgrade_coin)
        #self.font.draw(20, 130, "upgrade skill 'f' : need coin %2d" %monsters.upgrade_coin)
        self.font.draw(350, 90, "damage : %2d" %self.damage)
        if self.monster_count == 11:
            self.font.draw(30, 630, "boss time : %2d" %self.boss_time)