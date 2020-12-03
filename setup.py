import sys
import subprocess

def do_setup():
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-api-python-client'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-auth-httplib2'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade',
        'google-auth-oauthlib'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'termcolor'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'prettytable'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tabulate'])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print('\nInstalled Packages:\n')
    for _ in installed_packages:
        print('\t'+_)