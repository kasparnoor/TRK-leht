import configparser;
import os;
config = configparser.ConfigParser();

# Add the structure to the file we will create
config.add_section('version')
config.set('version', 'app', '1.0.0')
config.set('version', 'config', '1.0.0')
config.add_section('app')
config.set('app', 'debug', 'false')
config.set('app', 'date_simulation', 'false')
config.set('app', 'simulation_date', '2022, 5, 16, 9, 30')
config.set('app', 'timetable_url', 'https://real.edu.ee/oppimine/tunniplaan/tundide-algus/')
config.set('app', 'classes_url', 'https://real.edu.ee/oppetoo/tunniplaan/5per/Reaal/klassid/d5pe1A.htm')

config.add_section('database')
config.set('database', 'host', 'localhost')
config.set('database', 'db', 'postgres')
config.set('database', 'port', '3306')
config.set('database', 'user', 'user')
config.set('database', 'password', 'password')
# Write the new structure to the new file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'appconfig.ini'), 'w') as configfile:
    config.write(configfile)