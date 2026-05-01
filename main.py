class SettingsPage:
    def __init__(self):
        self.profile_section = ProfileSection()
        self.security_section = SecuritySection()
        self.notifications_section = NotificationsSection()

class ProfileSection:
    def __init__(self):
        self.name = "Profile"
        self.fields = [
            {"label": "Full Name", "value": ""},
            {"label": "Email", "value": ""},
            {"label": "Username", "value": ""}
        ]

    def render(self):
        print(f"**{self.name}**")
        for field in self.fields:
            print(f"{field['label']}: {field['value']}")

class SecuritySection:
    def __init__(self):
        self.name = "Security"
        self.fields = [
            {"label": "Password", "value": ""},
            {"label": "Two-Factor Authentication", "value": "Disabled"}
        ]

    def render(self):
        print(f"**{self.name}**")
        for field in self.fields:
            print(f"{field['label']}: {field['value']}")

class NotificationsSection:
    def __init__(self):
        self.name = "Notifications"
        self.fields = [
            {"label": "Email Notifications", "value": "Enabled"},
            {"label": "Push Notifications", "value": "Enabled"}
        ]

    def render(self):
        print(f"**{self.name}**")
        for field in self.fields:
            print(f"{field['label']}: {field['value']}")

class SettingsPageRenderer:
    def __init__(self, settings_page):
        self.settings_page = settings_page

    def render(self):
        self.settings_page.profile_section.render()
        self.settings_page.security_section.render()
        self.settings_page.notifications_section.render()

# Ustunlikni yaratish
settings_page = SettingsPage()

# Ustunlikni chiqarish
renderer = SettingsPageRenderer(settings_page)
renderer.render()
```

Kodda quyidagilar mavjud:

- `SettingsPage` - ustunlikni yaratish uchun klass.
- `ProfileSection`, `SecuritySection`, `NotificationsSection` - har bir ustunlik qismi uchun klass.
- `SettingsPageRenderer` - ustunlikni chiqarish uchun klass.
- `render` metodlari - har bir klass uchun ustunlik qismi va barcha ustunlik qismlarini chiqarish uchun metodlar.
- `fields` - har bir ustunlik qismida mavjud bo'lgan maydonlar uchun ro'yxat.
- `name` - har bir ustunlik qismi uchun nom.
- `SettingsPage` klassida ustunlik qismlari yaratiladi va `SettingsPageRenderer` klassida ustunlik qismlari chiqariladi.
