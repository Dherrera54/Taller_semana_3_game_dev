import esper

from src.ecs.components.c_animation import CAnimation
from src.ecs.components.tags.c_tag_explosion import CTagExplosion
from src.ecs.components.c_explosion_state import CExplosionState, ExplosionState


def system_explosion_state(world: esper.World):
    components = world.get_components(CAnimation, CExplosionState, CTagExplosion)
    for explosion_entity,(c_a, c_est, c_tag) in components:
        if c_est.state ==ExplosionState.START:
            _do_start_state(c_a,c_est)
        elif c_est.state == ExplosionState.END:
            _do_end_state(c_a,c_est,world, explosion_entity)
            

def _do_start_state(c_a:CAnimation,c_est:CExplosionState):
    _set_animation(c_a, 0)
    if c_a.curr_frame == c_a.animations_list[c_a.curr_anim].end:
        c_est.state = ExplosionState.END
def _do_end_state(c_a:CAnimation,c_pst:CExplosionState, world: esper.World, explosion_entity:int):
    _set_animation(c_a, 0)
    world.delete_entity(explosion_entity)

def _set_animation(c_a: CAnimation, num_anim: int):
    if c_a.curr_anim == num_anim:
         return
    c_a.curr_anim = num_anim
    c_a.curr_anim_time = 0
    c_a.curr_frame = c_a.curr_frame = c_a.animations_list[c_a.curr_anim].start