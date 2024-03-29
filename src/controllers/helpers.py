from .._const import app_name


def get_parent_to_root(env, id):
    cur_id = id

    path = []

    while cur_id and cur_id != 1:
        current_file = env[f'{app_name}.file'].browse([cur_id])

        current_file_dic = {}
        current_file_dic['link'] = f'/{current_file.type}/{current_file.id}'
        current_file_dic['label'] = current_file.name

        cur_id = current_file.parent.id
        path.insert(0, current_file_dic)

    path.insert(0, {'link': '/', 'label': 'root'})

    return path


def get_divisi_and_label(env):
    all_divisions_raw = env[f'{app_name}.divisi'].search([])
    all_divisions_name = []
    all_divisions_label = {}

    for divisi in all_divisions_raw:
        # Buat dapetin label
        label = dict(divisi._fields['name'].selection)[divisi.name]
        name = divisi.name

        all_divisions_label[name] = label
        all_divisions_name.append(name)

    return (all_divisions_name, all_divisions_label)


def remove_secrets(file):
    not_secret = True

    for tag in file.tags:
        if tag.name == 'secret':
            not_secret = False
            break

    return not_secret


def can_user_open(file, user):
    can = user.divisi.id in file.tags.ids
    secret_file = False
    for tag in file.tags:
        if tag.name == 'secret':
            secret_file = True
            break

    if secret_file:
        can = can and (user.jabatan.name ==
                       'admin' or user.jabatan.name == 'bod')

    return can


def get_tags_from_list_of_names(tags_name, env):
    tags = []
    for tag_name in tags_name:
        tag = env[f'{app_name}.file.tags'].search([('name', '=', tag_name)])
        tags.append((4, tag.id))

    return tags

def get_profiles_divisi(env, divisiName):
    divisi = env[f'{app_name}.divisi'].search([('name', '=', divisiName)])

    return divisi.profil
