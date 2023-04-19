

from src.create.prefab_creator import create_expolsion
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_hunter import CTagHunter


def system_collision_enemy_bullet(world: esper.World, expl_cfg:dict):
    components_enemy = world.get_components(CSurface, CTransform, CTagEnemy)
    components_bullet = world.get_components(CSurface, CTransform, CTagBullet)
    components_hunter = world.get_components(CSurface, CTransform, CTagHunter)
    
    for enemy_entity, (c_s, c_t, _) in components_enemy:
        ene_rect  = CSurface.get_area_relative(c_s.area, c_t.pos)

        
        for bullet_entity, (c_b_s, c_b_t, _) in components_bullet:
            bull_rect  = c_b_s.area.copy()
            bull_rect.topleft = c_b_t.pos
            
            if ene_rect.colliderect(bull_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)
                create_expolsion(world,c_t.pos, expl_cfg)

    for hunter_entity, (c_s, c_t, _) in components_hunter:
        ene_rect  = CSurface.get_area_relative(c_s.area, c_t.pos)

        
        for bullet_entity, (c_b_s, c_b_t, _) in components_bullet:
            bull_rect  = c_b_s.area.copy()
            bull_rect.topleft = c_b_t.pos
            
            if ene_rect.colliderect(bull_rect):
                world.delete_entity(hunter_entity)
                world.delete_entity(bullet_entity)
                create_expolsion(world,c_t.pos, expl_cfg)

