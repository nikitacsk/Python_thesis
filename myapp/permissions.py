from django.contrib.auth.mixins import UserPassesTestMixin


class LibrarianOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
