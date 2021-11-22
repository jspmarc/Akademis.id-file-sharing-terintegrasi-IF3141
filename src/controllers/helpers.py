from .._const import app_name


def get_parent_to_root(env, id):
    cur_id = id

    name = ''

    while cur_id != 1:
        current = env[f'{app_name}.file'].browse([id])
        name += f'/{current.name}'
        id = current.parent.id
