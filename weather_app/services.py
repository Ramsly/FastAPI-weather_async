from aiohttp import ClientSession


async def get_weather(city: str) -> dict | str:
    """
    Get weather from WeatherbitAPI
    :param city: str
    :return: city_weather - dict
    """
    async with ClientSession() as session:
        url = "https://api.weatherbit.io/v2.0/current"
        params = {'city': city, 'lang': 'en', 'key': '24318d7f9afb4d84b552f00f75c8a711'}
        async with session.get(url=url, params=params) as res:
            if res.status == 200:
                city_weather = await res.json()
                city_weather = {
                    'city': city,
                    'temp': city_weather['data'][0]['temp'],
                    'description': city_weather['data'][0]['weather']['description'],
                }
                return city_weather
            return f'status: {res.status} no content'
