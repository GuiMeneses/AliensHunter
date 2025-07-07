from code.Const import WIN_HEIGHT, ENT_METEOR_SCORE
from code.EntityProjectile import EntityProjectile
from code.PlayerStatus import PlayerStatus


class EntityMediator:
    def run(self, list_pj: list[list[EntityProjectile]], ps: PlayerStatus):
        self.verify_entity_in_screen(list_pj[0], -33)
        self.verify_entity_in_screen(list_pj[1], WIN_HEIGHT)
        self.verify_collision_player_shot_to_entity(list_pj[0], list_pj[1], ps)

    def verify_entity_in_screen(self, list_entity: list[EntityProjectile], limit: int):
        for pj in list_entity:
            if limit > 0:
                if pj.position[1] > limit:
                    list_entity.remove(pj)

            elif pj.position[1] < limit:
                list_entity.remove(pj)


    def verify_collision_player_shot_to_entity(self, list_player_shot: list[EntityProjectile], list_entity: list[EntityProjectile], ps):

        for player_projectile in list_player_shot:
            for ent in list_entity:
                if player_projectile.rect.colliderect(ent.rect):
                    ent.health -= player_projectile.damage_collision
                    list_player_shot.remove(player_projectile)
                    if self.verify_helth_ent(ent):
                        if ent.img_png == './Assets/meteor.png':
                            ps.score += ENT_METEOR_SCORE




                        list_entity.remove(ent)


    def verify_helth_ent(self, entity: EntityProjectile):
        if entity.health <= 0:
            return True

    def explosion(self):
        explosion = Entity()



