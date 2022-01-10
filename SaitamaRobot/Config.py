from SaitamaRobot.sample_config import Config

class Development(Config):
    OWNER_ID = 1511373882  # your telegram ID
    OWNER_USERNAME = "its_pranav_xd"  # your telegram username
    API_KEY = "5030042183:AAFCJuOd-R4n06Pk9RFuLg3MnFPrMCz2uGA"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:AI4yXvnnjKAhuGdVIHwE@containers-us-west-22.railway.app:7098/railway'  # sample db credentials
    JOIN_LOGGER = '1276224293' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
