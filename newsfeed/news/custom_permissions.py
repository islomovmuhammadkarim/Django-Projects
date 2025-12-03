from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



class OnlySuperUser(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class OnlyAuthorOrSuperUser(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user == self.get_object().author

class OnlyStaffUser(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
