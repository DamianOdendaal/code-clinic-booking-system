# import os
import sys
import subprocess
import os


def install_packages():
    """
    This function will load all the necessary modules needed to run the wtc-cal
    """

    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-api-python-client'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-auth-httplib2'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-auth-oauthlib'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'termcolor'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ics'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jsonlib-python3'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'icalendar'])

    print("\nSetup completed!\n")


if os.path.exists(f"{sys.path[0]}/files/json/.config.json") == False:
    install_packages()