from os import environ


class BaseHandler(object):
    def __init__(self, actor):
        self._base_url = environ.get("BASE_URL") or 'http://18.195.167.117:5000'
        self.timeout = 10
        self.actor = actor

    def _make_request(self, url, method,
                      params=None, files=None, json=None, timeout=None, headers=None, cookies=None, **kwargs):
        if timeout is None:
            timeout = self.timeout

        if not url.startswith("/"):
            url = "/" + url

        # Send request
        response = self.actor.session.request(
            url=self._base_url + url,
            method=method,
            params=params,
            files=files,
            json=json,
            timeout=timeout,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

        return response

    def _get(self, url, params=None, headers=None, cookies=None):
        return self._make_request(
            method="GET",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies
        )

    def _post(self, url, params=None, json=None, files=None, headers=None, cookies=None):
        return self._make_request(
            method="POST",
            url=url,
            json=json,
            files=files,
            params=params,
            headers=headers,
            cookies=cookies
        )

    def _delete(self, url, headers=None, cookies=None):
        return self._make_request(
            method="DELETE",
            url=url,
            headers=headers,
            cookies=cookies
        )