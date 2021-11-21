from .._const import complete_app_name


def render_err(req, err_code):
    return req.render(f'{complete_app_name}.error_{err_code}')
