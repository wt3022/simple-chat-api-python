from django.contrib.admin.apps import AdminConfig as DefaultAdminConfig


class AdminConfig(DefaultAdminConfig):
    default_site = "src.admin.AdminSite"
