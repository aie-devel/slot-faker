from faker.providers import BaseProvider


class Provider(BaseProvider):

    notification_destinations = (
        'phone',
        'tablet',
        'computer',
        'mail'
    )

    notification_methods = (
        'text',
        'SMS',
        'telephone',
        'call',
        'email',
        'mail'
    )

    device_purpose = (
        'Personal',
        'Business'
    )

    resolutions = (
        '720p',
        '1080p',
        'HD'
        '2k',
        'UHD',
        '4K',
        '8K'
    )

    operating_systems = (
        'iOS',
        'iPadOS',
        'macOS',
        'Windows',
        'Ubuntu',
        'Red Hat Enterprise Linux', 'RHEL',
        'Fedora',
        'Chrome OS',
        'Android'
    )

    os_releases = {
        'macOS': (
            '10.0', 'Cheetah',
            '10.1', 'Puma',
            '10.2', 'Jaguar',
            '10.3', 'Panther',
            '10.4', 'Tiger',
            '10.5', 'Leopard',
            '10.6', 'Snow Leopard',
            '10.7', 'Lion',
            '10.8', 'Mountain Lion',
            '10.9', 'Mavericks',
            '10.10', 'Yosemite',
            '10.11', 'El Capitan',
            '10.12', 'Sierra',
            '10.13', 'High Sierra',
            '10.14', 'Mojave',
            '10.15', 'Catalina',
            '11', 'Big Sur'
        ),
        'iPadOS': ('13', '14'),
        'iOS': (
            '4', '5', '6', '7', '8', '9',
            '10', '11', '12', '13', '14'
        ),
        'Windows': (
            '10', '10 Mobile',
            '8.1', '8',
            '7',
            'Vista',
            'XP', 'XP Professional',
            'Me',
            '2000',
            '98',
            '95',
            'Phone 7',
            'Phone 8',
            'Phone 8.1'
        ),
        'Ubuntu': (
            '21.04', 'Hirsute Hippo',
            '20.10', 'Groovy Gorilla',
            '20.04', 'Focal Fossa',
            '19.10', 'Eoan Ermine',
            '19.04', 'Disco Dingo',
            '18.10', 'Cosmic Cuttlefish',
            '18.04 LTS', 'Bionic Beaver'
        ),
        'Red Hat Enterprise Linux': ('6', '7', '8'),
        'RHEL': ('6', '7', '8'),
        'Fedora': (
            '26', '27', '28', '29',
            '30', '31', '32', '33'
        ),
        'Chrome OS': ('M82', 'M83', 'M84'),
        'Android': (
            '11', '10',
            '9', 'Pie',
            '8.0', 'Oreo',
            '7.0', 'Nougat',
            '6.0', 'Marshmallow',
            '5.0', 'Lollipop',
            '4.4', 'KitKat',
            '4.1', 'Jelly Bean'
        )
    }

    def notification_destination(self):
        return self.random_element(self.notification_destinations)

    def notification_method(self):
        return self.random_element(self.notification_methods)

    def resolution(self):
        return self.random_element(self.resolutions)

    def device_purpose(self):
        return self.random_element(self.device_purposes)

    def operating_system(self):
        return self.random_element(self.operating_systems)

    def os(self):
        return self.operating_system()

    def os_release(self):
        os = self.operating_system()
        return f"{os} {self.random_element(self.os_releases[os])}"