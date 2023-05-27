import json
from flask.json.provider import JSONProvider


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__') and callable(getattr(obj, '__json__')):
            return obj.__json__()
        return super().default(obj)


class CustomJsonProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=CustomJSONEncoder)

    def loads(self, s: str, **kwargs):
        return json.loads(s, **kwargs)
