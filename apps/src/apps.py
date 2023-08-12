from django.contrib.admin.apps import AdminConfig as DefaultAdminConfig


class AdminConfig(DefaultAdminConfig):
    """
    デフォルトの admin サイトをカスタマイズ

    References:
        https://docs.djangoproject.com/ja/2.2/ref/contrib/admin/#overriding-the-default-admin-site

    """

    default_site = "src.admin.AdminSite"
