import esper
import pygame
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_enemy_state import CEnemyState, EnemyState

def system_enemy_state(world:esper.World, player_entity:int, enemy_cfg:dict):
    components = world.get_components(CVelocity, CAnimation, CTransform, CEnemyState)
    pl_t = world.component_for_entity(player_entity, CTransform)
    for _,(c_v, c_a, c_t, c_est) in components:
        if c_est.state ==EnemyState.IDLE:
            _do_idle_state(c_v,c_a,c_t, c_est, pl_t, enemy_cfg)
        elif c_est.state == EnemyState.MOVE:
            _do_move_state(c_v,c_a,c_t, c_est, pl_t, enemy_cfg)

def _do_idle_state(c_v:CVelocity,c_a:CAnimation,c_t: CTransform, c_est:CEnemyState, pl_t:CTransform, enemy_cfg:dict):
    _set_animation(c_a, 1)
     
    d_pl = c_t.pos.distance_to(pl_t.pos)
    if d_pl<=enemy_cfg["distance_start_chase"]:   
        c_est.state = EnemyState.MOVE


def _do_move_state(c_v:CVelocity,c_a:CAnimation,c_t: CTransform, c_est:CEnemyState, pl_t:CTransform, enemy_cfg:dict):
    _set_animation(c_a, 0)

    d_pl = c_t.pos.distance_to(pl_t.pos)
    c_est_pos=pygame.Vector2(c_est.pos_x, c_est.pos_y)
    d_o=c_t.pos.distance_to(c_est_pos)
    
    if d_pl<=enemy_cfg["distance_start_chase"] and d_o<enemy_cfg["distance_start_return"]:
        c_v.vel= (pl_t.pos-c_t.pos).normalize()*enemy_cfg["velocity_chase"]
    
    
    elif d_o>enemy_cfg["distance_start_return"]:
        c_v.vel= (c_est_pos-c_t.pos).normalize()*enemy_cfg["velocity_return"]
    elif d_o<1:      
        c_v.vel.x = 0
        c_v.vel.y = 0   
        c_est.state = EnemyState.IDLE 
    
""" def _do_returnung_state(c_v:CVelocity,c_a:CAnimation,c_t: CTransform, c_est:CEnemyState, pl_t:CTransform, enemy_cfg:dict):
    _set_animation(c_a, 0)
    
    c_v.vel= (pl_t.pos-c_t.pos).normalize()*enemy_cfg["velocity_chase"]
    c_est_pos=pygame.Vector2(c_est.pos_x, c_est.pos_y)
    d_o=c_t.pos.distance_to(c_est_pos)
    
    if d_o>enemy_cfg["distance_start_return"]:
        c_v.vel= (c_est_pos-c_t.pos).normalize()*enemy_cfg["velocity_return"]
        c_est.state = EnemyState.RETURNING
    print(d_o)
    if d_o<0:      
        c_v.vel =  [0,0]     
        c_est.state = EnemyState.IDLE  """

def _set_animation(c_a: CAnimation, num_anim: int):
    if c_a.curr_anim == num_anim:
        return
    c_a.curr_anim = num_anim
    c_a.curr_anim_time = 0
    c_a.curr_frame = c_a.curr_frame = c_a.animations_list[c_a.curr_anim].start