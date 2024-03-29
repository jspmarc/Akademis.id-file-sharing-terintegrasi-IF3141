from .._const import complete_app_name


def render_err(req, err_code, err_msg):
    return req.render(f'{complete_app_name}.error', {
        'data_err_code': err_code,
        'data_err_msg': err_msg,
    })
