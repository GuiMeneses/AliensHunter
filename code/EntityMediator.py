import pygame

from code.AlienShot import AlienShot
from code.Animation import Animation
from code.Const import WIN_HEIGHT, PS_METEOR_SCORE, SOUND_DELAY_HURT, PS_DAMAGE_COLLISION, PS_ALIEN_SCORE, \
    ALIEN_SHOT_DAMAGE
from code.EntityAnim import EntityAnim
from code.EntityPlayer import EntityPlayer
from code.EntityProjectile import EntityProjectile
from code.MyTimer import MyTimer


class EntityMediator:
    def __init__(self, screen, sound_explosion, sound_hurt, sound_energy, entity_player, ps):
        self.screen = screen
        self.sound_explosion = sound_explosion
        self.sound_hurt = sound_hurt
        self.sound_energy = sound_energy
        self.entity_player = entity_player
        self.ps = ps
        self.timer_hurt = MyTimer(SOUND_DELAY_HURT)

    def run(self, list_pj: list[list[EntityProjectile]], list_animation: list[Animation],
            list_alien_shot: list[AlienShot], list_energy: list[EntityAnim]):
        self.verify_entity_in_screen(list_pj[0], -33)
        self.verify_entity_in_screen(list_pj[1], WIN_HEIGHT)
        self.verify_collision_player_shot_to_entity(list_pj[0], list_pj[1], list_animation)
        self.verify_collision_player_to_entity(self.entity_player, list_pj[1])
        self.timer_hurt.run()
        self.verify_alien_shot_in_window(list_alien_shot)
        self.verify_player_to_alien_shot(self.entity_player, list_alien_shot)
        self.verify_player_to_energy(self.entity_player, list_energy)

    def verify_entity_in_screen(self, list_entity: list[EntityProjectile], limit: int):
        to_remove = []
        for pj in list_entity:
            if limit > 0:
                if pj.position[1] > limit:
                    to_remove.append(pj)
            elif pj.position[1] < limit:
                to_remove.append(pj)
        for pj in to_remove:
            if pj in list_entity:
                list_entity.remove(pj)

    def verify_collision_player_shot_to_entity(self,
                                               list_player_shot: list[EntityProjectile],
                                               list_entity: list[EntityProjectile],
                                               list_animation: list[Animation]):
        to_remove_pj = []
        to_remove_entity = []

        for player_projectile in list_player_shot:
            for ent in list_entity:
                if player_projectile.rect.colliderect(ent.rect):
                    ent.health -= player_projectile.damage_collision
                    to_remove_pj.append(player_projectile)

                    if self.verify_helth_ent(ent):
                        anim = Animation(
                            image_paths='./Assets/Explosion_',
                            frame_delay=100,
                            pos=(ent.position[0] - 80, ent.position[1] - 49),
                            size=(196, 196),
                            loop=False
                        )
                        list_animation.append(anim)
                        self.sound_explosion.play()

                        if ent.img_png == './Assets/meteor.png':
                            self.ps.score += PS_METEOR_SCORE
                        elif ent.img_png == './Assets/Alien_ship.png':
                            self.ps.score += PS_ALIEN_SCORE

                        to_remove_entity.append(ent)

        for pj in to_remove_pj:
            if pj in list_player_shot:
                list_player_shot.remove(pj)

        for ent in to_remove_entity:
            if ent in list_entity:
                list_entity.remove(ent)

    def verify_helth_ent(self, entity: EntityProjectile):
        return entity.health <= 0

    def verify_collision_player_to_entity(self,
                                          player: EntityPlayer,
                                          list_entity: list[EntityProjectile]):
        for ent in list_entity:
            if player.rect.colliderect(ent.rect):
                self.ps.subtract_health(PS_DAMAGE_COLLISION)
                if self.timer_hurt.seconds >= SOUND_DELAY_HURT:
                    self.timer_hurt.start_time = pygame.time.get_ticks()
                    self.sound_hurt.play()

    def verify_alien_shot_in_window(self, list_alien_shot: list[AlienShot]):
        to_remove = []
        for shot in list_alien_shot:
            if shot.rect.top > WIN_HEIGHT:
                to_remove.append(shot)
        for shot in to_remove:
            if shot in list_alien_shot:
                list_alien_shot.remove(shot)

    def verify_player_to_alien_shot(self, player: EntityPlayer, list_alien_shot: list[AlienShot]):
        to_remove = []
        for shot in list_alien_shot:
            if player.rect.colliderect(shot.rect):
                self.sound_hurt.play()
                self.ps.subtract_health(ALIEN_SHOT_DAMAGE)
                to_remove.append(shot)
        for shot in to_remove:
            if shot in list_alien_shot:
                list_alien_shot.remove(shot)

    def verify_player_to_energy(self, player: EntityPlayer, list_energy: list[EntityAnim]):
        to_remove = []
        for ent in list_energy:
            if player.rect.colliderect(ent.rect):
                self.sound_energy.play()
                self.ps.add_energy(10)
                to_remove.append(ent)
        for ent in to_remove:
            if ent in list_energy:
                list_energy.remove(ent)
