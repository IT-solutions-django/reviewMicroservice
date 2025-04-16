import enum


class SettingRequest(enum.Enum):
    headers = {
        'Host': 'yandex.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Cookie': 'maps_los=0; spravka=dD0xNzI2ODEwMTY3O2k9ODYuMTAyLjEzLjc0O0Q9RUY3MDRCMEVFNzU0MTg1N0YzNTZENDg2RjlGMjNFNDMzNTY2NDdDRUQxQzlFQzE3NTFEQThDREFGMjA4MTNFNENFMUFFNkQyRTNCOTBGRTc3NENEOEJFQTExNUVFNjQwRUQwOEIwNDQ2QjI0NUYyRkVBQkEwMzNEMzQxM0JFNzA1MEQ0MzMyOTlGRkY1M0I4MUJERDt1PTE3MjY4MTAxNjc2NTgyNzE1ODA7aD01YmYzMGNlNTBmYTY4ODljZWI0ZmM5NjcyOTI4MGJmOQ==; _yasc=r3AyN1rNx3P7SuIwvwYQHGPC7jhpypevF0XoRv0aqOsiu8Q5dsPbKyhN0qIj9ZEhnAHqypxgYP8=; i=USTWwFikzzttv4Ewt+JjX6guEjI7ryOi3U8d1d0obMvWdQLf6l3nC4o08OxIR2X5+xwqxB4bIfVflox4XzmFHzUvDKI=; yandexuid=1948173161726810137; yashr=8704804031726810137; receive-cookie-deprecation=1; yuidss=1948173161726810137; ymex=2042170139.yrts.1726810139; _ym_uid=1726810140413132111; _ym_d=1726810140; is_gdpr=0; is_gdpr_b=CLmcHRCIlAIoAg==; yp=2042170169.pcs.1#1729488569.hdrc.0#1727414969.szm.0_8:2400x1350:2400x1194; bh=YNvqsLgGahfcyuH/CJLYobEDn8/14QyChPKOA4vBAg==; yabs-vdrf=A0; gdpr=0',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
    }

    url = 'https://yandex.ru/maps/org/{organization_slug}/{organization_id}/reviews/'

    @classmethod
    def get_url(cls, organization_slug, organization_id):
        return cls.url.value.format(organization_slug=organization_slug, organization_id=organization_id)
