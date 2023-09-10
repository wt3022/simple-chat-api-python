from django.contrib.admin import AdminSite as DefaultAdminSite


class AdminSiteSettingMixin:
    ordered_models = {"accounts": ["User"]}

    ordered_apps = [
        "accounts",
    ]

    exclude_apps = [
        "authtoken",
        "auth",
    ]

    def get_model_sort_func(self, app_label):
        def sort_key(model):
            model_names = self.ordered_models.get(app_label)

            if not model_names or model["object_name"] not in model_names:
                return "9999_{}".format(model["name"].lower())

            return str(model_names.index(model["object_name"]))

        return sort_key

    def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request, app_label)
        app_dict = {k: v for k, v in app_dict.items() if k not in self.exclude_apps}

        def key_fnc(app_label):
            if app_label not in self.ordered_apps:
                return "9999_{}".format(app_label.lower())
            idx = self.ordered_apps.index(app_label)
            return f"{idx:04}"

        app_list = sorted(app_dict.values(), key=lambda x: key_fnc(x["app_label"]))

        for app in app_list:
            app["models"].sort(key=self.get_model_sort_func(app["app_label"]))

        return app_list


class AdminSite(AdminSiteSettingMixin, DefaultAdminSite):
    pass
