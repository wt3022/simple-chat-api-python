from django.conf import settings
from django.db import models

from src.middleware import get_current_authenticated_user


class CurrentUserField(models.ForeignKey):
    """認証済みリクエストユーザーを保存します。"""

    defaults = dict(null=True, default=get_current_authenticated_user, to=settings.AUTH_USER_MODEL)

    def __init__(self, **kwargs):
        self.on_update = kwargs.pop("on_update", False)

        if "on_delete" not in kwargs:
            kwargs["on_delete"] = models.CASCADE

        if self.on_update:
            kwargs["editable"] = False
            kwargs["blank"] = True

        kwargs.update(self.defaults)
        super(CurrentUserField, self).__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CurrentUserField, self).deconstruct()
        if self.on_update:
            kwargs["on_update"] = self.on_update
            del kwargs["editable"]
            del kwargs["blank"]

        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        if self.on_update:
            value = get_current_authenticated_user()
            if value is not None:
                value = value.pk
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(CurrentUserField, self).pre_save(model_instance, add)
