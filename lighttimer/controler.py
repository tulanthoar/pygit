'''backlight controller to act as pomodoro reminder'''
from time import sleep
from os import W_OK
from path import Path
from sh import xset, xmessage


def backlight_set():
    '''dim the backlight after a set number of minutes'''
    bl_path = Path('/sys/class/backlight/intel_backlight/brightness')
    assert bl_path.access(W_OK)
    maxb_path = Path('/sys/class/backlight/intel_backlight/max_brightness')
    maxb = maxb_path.text().strip()
    maxb = '%d' % (int(maxb) // 1.2)
    while True:
        try:
            xset('dpms', 'force', 'on')
            bl_path.write_text(maxb)
            sleep(60*18)
            bl_path.write_text('300')
            sleep(60*2)
            cnt = 0
            step = 15
            minutes = 10
            while cnt < minutes*60:
                xmessage('-timeout', str(step-1), str(minutes*60-cnt))
                xset('dpms', 'force', 'off')
                sleep(step)
                cnt += step
        finally:
            bl_path.write_text(maxb)
    xset('dpms', 'force', 'on')


backlight_set()
