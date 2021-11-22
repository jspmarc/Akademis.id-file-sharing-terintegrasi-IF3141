import logging
from .._const import app_name


def get_parent_to_root(env, id):
    cur_id = id

    path = []
    logger = logging.getLogger(__name__)

    while cur_id and cur_id != 1:
        logger.info('-----------------------')
        logger.info(cur_id)
        logger.info('-----------------------')
        current_file = env[f'{app_name}.file'].browse([id])

        current_file_dic = {}
        current_file_dic['link'] = f'/{current_file.type}/{current_file.id}'
        current_file_dic['label'] = current_file.name

        cur_id = current_file.parent.id
        path.insert(0, current_file_dic)

    path.insert(0, {'link': '/', 'label': 'root'})

    logger.info('-----------------------')
    logger.info(path)
    logger.info('-----------------------')

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
