import enum


class SettingRequest(enum.Enum):
    headers = {
        "Host": "www.vl.ru",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.vl.ru/autocenter",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    cookies = {
        "PHPSESSID": "rhjcp9pkfg82bvcda7tve2a9m0",
        "city": "4",
        "region": "103",
        "visitor": "ad5f2acbb35cd457a9dc57c692437d9261e1d5606ea33280caabd64f0fa3d0d6",
        "ring": "980791ab6a297547f26234387e1a5012",
        "analytics_user": "980791ab6a297547f26234387e1a5012",
        "spravochnik_windowSessionID": "ad061bf1730033306880",
        "_ym_uid": "1730033307709177970",
        "_ym_d": "1730033307",
        "sprRecentlyWatchedCompanyIds": "460034",
        "_ym_isad": "2",
        "_gid": "GA1.2.1877505797.1730033311",
        "_ga": "GA1.3.1517315620.1730033307",
        "_ga_3XHX5WMXEB": "GS1.2.1730033312.1.0.1730033312.60.0.0",
        "_ga_D3RZ9TRN3Y": "GS1.3.1730033312.1.0.1730033312.60.0.0",
        "_ga_1XW1PCV9KF": "GS1.2.1730033312.1.1.1730034975.8.0.0",
        "_ym_visorc": "w",
        "spravochnik_windowSessionTS": "1730035316115",
        "_ga_3X07YH0D78": "GS1.1.1730035314.2.1.1730035316.0.0.0",
        "_gat": "1",
        "_gat_allProjects": "1",
        "_gat_glCommonTracker": "1",
        "_gat_commentsvlru": "1",
    }
