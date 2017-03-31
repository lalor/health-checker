def sync_error(action_name, error, **kwargs):
    resp_dict = {}

    resp_dict['action'] = action_name
    resp_dict['is_success'] = False
    error = str(error) if isinstance(error, Exception) else error
    resp_dict['error'] = error

    if kwargs:
        resp_dict.update(kwargs)

    return resp_dict

def sync_ok(action_name, body, **kwargs):
    resp_dict = {}

    resp_dict['action'] = action_name
    resp_dict['is_success'] = True
    resp_dict['body'] = body

    if kwargs:
        resp_dict.update(kwargs)

    return resp_dict
