from config import Config
import time



class LogoHandler:
    def write_logo(is_timespan_logo, text):
        
        logo_text = ""
        
        if (is_timespan_logo):
            str_timespan = time.strftime('[%Y-%m-%d %H:%M:%S]')
            logo_text = str_timespan + ' - ' + text

        else:
            logo_text = text


        with open(Config.LOGO_FILE_PATH, mode='a', encoding='utf-8') as file:
            file.write(logo_text)

