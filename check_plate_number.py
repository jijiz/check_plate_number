
import subprocess as sp, shlex
import time

while (1):
    sp.Popen(shlex.split('fswebcam -r 1920x1080 --no-banner plate_number.jpg -q'))
    process = sp.Popen(shlex.split('alpr -c eu -n 1 plate_number.jpg'),stdout=sp.PIPE,stderr=sp.PIPE)
    out, err = process.communicate()
    if 'No license' in out:
        print("AUCUNE VOITURE")
    elif 'XXX' in out or 'YYY' in out or 'ZZZ' in out:
        print("BMW")
    elif 'EEE' in out:
        print("ZOE")
    else:
        print("PB",out)
