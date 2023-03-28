import requests
import json

# Surpress ssl warnings
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)


actions = {
    'verify': 'chkca',
    'check_current': 'viewitn',
    'check_planned': 'viewitn_plan'
}


def _get_outages_data(client_id, check_type):
    if isinstance(client_id, int):
        client_id = str(client_id)

    data = {
        'action': actions[check_type],
        'itn': client_id
    }

    response = requests.post('https://info.electrohold.bg/webint/vok/avplan.php', data=data, verify=False)
    response_data_raw = response.text.encode().decode('utf-8-sig')
    
    return response_data_raw


def get_outages(client_id, debug=False):
    steps = actions.keys()

    ret_data = dict()

    for step in steps:
        raw_data = _get_outages_data(client_id, step)

        if debug:
            print(f"{raw_data=}")

        if "няма планирани прекъсвания" in raw_data or "няма регистрирано планирано" in raw_data:
            ret_data[step] = None
        else:
            ret_data[step] = json.loads(raw_data)
    
    return ret_data


def main():
    print(get_outages('300066244165'))


if __name__ == "__main__":
    main()
