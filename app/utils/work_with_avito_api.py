import requests

KEY = "af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir"

headers = {
 'cookie': 'u=2k95bf7i.pxs8fw.5e0zarct1sk0; buyer_laas_location=639720; buyer_selected_search_radius4=0_general; __cfduid=d615f7edcf8dad3eb3f5fb12986b2c5901605966252; showedStoryIds=51-50-49-48-47-46-45-43-41-42-39-32-30-25; lastViewingTime=1605966253902; _ym_uid=15976593101054249299; _ym_d=1605966254; _ga=GA1.2.1870418395.1605966254; _fbp=fb.1.1605966254711.2048695945; __gads=ID=eb6acdb524899186:T=1605966254:S=ALNI_MbMpUwnntW60ZF_W7zZepBkrdLJ2g; isCriteoSetNew=true; buyer_location_id=639410; luri=sverdlovskiy; sessid=d4bde536e3fb424c9837b371afda8c15.1606119234; abp=2; no-ssr=1; _gid=GA1.2.456152918.1606119237; _ym_isad=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9c7f279391b0a395990d83bac5e6e82bd59c9621b2c0fa58f915ac1de0d0341125ba970d9f9a26a3a3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da79c1784b8149a5786bdb615eb0358b0e42985db2d99140e2dad16df6476ce10923aa693184fc0885138f0f5e6e0d2832e0f00959afa40dceaecddefc274cef47e46b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac9317cdb1f8e40fc8395e66c0f17481e32da10fb74cac1eab2da10fb74cac1eab25037f810d2d41a8134ecdeb26beb8b5ff8d13bbf5e8eb298012e98924060d02; _gcl_au=1.1.660167445.1606156386; v=1606162082; _ym_visorc_34241905=b; _ym_visorc_189903=w; sx=H4sIAAAAAAACA1XNMQ7CMAxA0bt47uCAaZ0epylYxTQpWKqFqtydMDCwP%2F1%2FwIRIeI7huamrcxFLjpKKwXjADiMsW8Z1vQ%2BcCYsooYh%2BqRYvbgYdXGEMPfYnYoqhdjDnN%2B8PXmZqRNzc2dqF8Je8pOE1xcD5JuKkiI0VUmHXxOT%2FSY61fgAnipnMpwAAAA%3D%3D; _ym_visorc_26812653=b; buyer_from_page=catalog',
 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


def get_count(text: str, region: str) -> (int, int):
    r = requests.get(f"https://m.avito.ru/api/9/items?key={KEY}&query={text}&locationId={region}", headers=headers)
    return r.json()["result"]["mainCount"], r.json()["result"]["lastStamp"]
