from path import Path
from time import sleep
from os import W_OK
from sh import xset,xmessage

bl=Path('/sys/class/backlight/intel_backlight/brightness')
assert(bl.access(W_OK))
maxb=Path('/sys/class/backlight/intel_backlight/max_brightness').text().strip()
maxb = '%d' % (int(maxb) // 1.2)
while True:
    try:
        xset('dpms', 'force', 'on')
        bl.write_text(maxb)
        sleep(60*18)
        bl.write_text('300')
        sleep(60*2)
        cnt=0
        step=15
        minutes=10
        while cnt < minutes*60:
            xmessage('-timeout', str(step-1), str(minutes*60-cnt))
            xset('dpms', 'force', 'off')
            sleep(step)
            cnt+=step
    finally:
        bl.write_text(maxb)
xset('dpms', 'force', 'on')
