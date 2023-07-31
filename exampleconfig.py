from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24377655
    API_HASH = "dcc4df6e24ceedebd424c6db9a7194f8"
    # the name to display in your alive message
    ALIVE_NAME = "ghost"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "BQBudL0g5DvlAkNkyh4kbr2hnIirRHgCxv7NmWKsdb8pR0luDbbqmvlSiRdEjEHs5NpJiCM_qsxN0aTfZn7vlWovYsyXoDuRYUfUxEfQQAC1YepNCF93_G4a6J2AwXccYLVc6wc56fKPerREovE-gv8yZj_vSTZqwwxSaiZOf7NfxNbpGvWw8UQNZSzgqVYW99rCliDzWs3fMTPftv81ktuUoTmkOF8SgRTpYXa7EAJshbCSUgUuKDqLqdLjTKp0Kwfnrko5sS_NDEjAH8YHe3Lk77zvh6r6X1mOVQ1ocfVsztAOt_dFSLyhf96Db5rgFTGIh87aSVbQhln-_lgc8Ym6AAAAAT2WWAIA"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6217733896:AAEtaF6mkAOEO6UEn8WUkhYu987pim_Tp0U"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
