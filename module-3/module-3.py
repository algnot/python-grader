import json

def censor_keys(data, keys_to_censor):
    if isinstance(data, dict):
        return {
            k: ("****" if k in keys_to_censor else censor_keys(v, keys_to_censor))
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [censor_keys(item, keys_to_censor) for item in data]
    else:
        return data

def input_func(input_json):
    keys_to_censor = {"email", "password"}
    try:
        input_data = json.loads(input_json)
        censored_data = censor_keys(input_data, keys_to_censor)
        return json.dumps(censored_data, ensure_ascii=False)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input")