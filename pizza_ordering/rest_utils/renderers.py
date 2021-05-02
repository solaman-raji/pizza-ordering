from rest_framework.renderers import JSONRenderer


class APIJSONRenderer(JSONRenderer):
    base_format = {
        "message": "",
    }

    success_format = {
        "success": True,
        "meta": {},
        **base_format
    }

    failure_format = {
        "success": False,
    }

    def set_error_response(self, data):
        errors = data.get("errors")
        message = data.get("message")
        self.failure_format["error"] = errors
        self.base_format["message"] = message
        self.failure_format.update(**self.base_format)

    def get_proper_response(self, data):
        meta = dict()

        if isinstance(data, dict):
            if "meta" in data.keys():
                meta = data.pop("meta")

            errors = data.get("errors")

            if errors:
                self.set_error_response(data=data)

                return self.failure_format

            self.success_format.update(
                data=data,
                meta=meta
            )

            return self.success_format

        self.success_format.update(
            data={
                "results": data,
                "count": len(data) if data else 0
            }
        )

        return self.success_format

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = self.get_proper_response(data=data)

        return super().render(
            data=data,
            accepted_media_type=accepted_media_type,
            renderer_context=renderer_context
        )
