import pygame

from code.AlienShot import AlienShot
from code.Animation import Animation
from code.Const import WIN_HEIGHT, PS_METEOR_SCORE, SOUND_DELAY_HURT, PS_DAMAGE_COLLISION, PS_ALIEN_SCORE
from code.EntityPlayer import EntityPlayer
from code.EntityProjectile import EntityProjectile
from code.MyTimer import MyTimer


class EntityMediator:
    def __init__(self, screen, sound_explosion, sound_hurt, entity_player, ps):
        self.screen = screen
        self.sound_explosion = sound_explosion
        self.sound_hurt = sound_hurt
        self.entity_player = entity_player
        self.ps = ps
        self.timer_hurt = MyTimer(SOUND_DELAY_HURT)

    def run(self, list_pj: list[list[EntityProjectile]], list_animation: list[Animation]):
        self.verify_entity_in_screen(list_pj[0], -33)
        self.verify_entity_in_screen(list_pj[1], WIN_HEIGHT)
        self.verify_collision_player_shot_to_entity(list_pj[0], list_pj[1], list_animation)
        self.verify_collision_player_to_entity(self.entity_player, list_pj[1])
        self.timer_hurt.run()

    def verify_entity_in_screen(self, list_entity: list[EntityProjectile], limit: int):
        for pj in list_entity:
            if limit > 0:
                if pj.position[1] > limit:
                    list_entity.remove(pj)

            elif pj.position[1] < limit:
                list_entity.remove(pj)

    def verify_collision_player_shot_to_entity(self,
                                               list_player_shot: list[EntityProjectile],
                                               list_entity: list[EntityProjectile],
                                               list_animation: list[Animation]):

        for player_projectile in list_player_shot:
            for ent in list_entity:
                if player_projectile.rect.colliderect(ent.rect):
                    ent.health -= player_projectile.damage_collision
                    list_player_shot.remove(player_projectile)
                    if self.verify_helth_ent(ent):
                        anim = Animation(image_paths='./Assets/Explosion_', frame_delay=100,
                                         pos=(ent.position[0] - 80, ent.position[1] - 49),
                                         size=(196, 196),
                                         loop=False)
                        # Meteor destroy
                        if ent.img_png == './Assets/meteor.png':
                            list_animation.append(anim)
                            self.sound_explosion.play()
                            self.ps.score += PS_METEOR_SCORE
                        # Alien destroy END
                            # Meteor destroy
                        if ent.img_png == './Assets/Alien_ship.png':
                            list_animation.append(anim)
                            self.sound_explosion.play()
                            self.ps.score += PS_ALIEN_SCORE
                        # Alien destroy END
                        list_entity.remove(ent)

    def verify_helth_ent(self, entity: EntityProjectile):
        if entity.health <= 0:
            return True
        return None

    def verify_collision_player_to_entity(self,
                                          player: EntityPlayer,
                                          list_entity: list[EntityProjectile]):
        for ent in list_entity:
            if player.rect.colliderect(ent.rect):
                self.ps.subtract_health(PS_DAMAGE_COLLISION)
                if self.timer_hurt.seconds >= SOUND_DELAY_HURT:
                    self.timer_hurt.start_time = pygame.time.get_ticks()
                    self.sound_hurt.play()
                if self.ps.health <= 0:
                    print('game over')





