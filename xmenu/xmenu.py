'''menu to interface with xmonad'''
from time import sleep
from click import echo, getchar, command
from sh import Command
from ewmh import EWMH


def class_is_visible(hinter, class_name):
    '''check if a window with class_name is currently visible'''
    for win in hinter.getClientListStacking():
        if class_name in win.get_wm_class():
            return win.get_wm_state()['state'] == 1
    return None


def print_menu(persist):
    '''print menu of available keys'''
    echo('Spc: next empty ws')
    echo('Tab: toggle persist')
    echo('  c: clipmenu')
    echo('  q: qutebrowser')
    echo('  j: j4-app-menu')
    echo('  n: neovim')
    echo('  i: ipython')
    echo('  p: perl repl')
    echo('  r: ranger')
    echo('  a: all pads')
    echo('  P: pomodoro')
    echo('  h: htop')
    echo('  u: urxvt')
    if persist:
        echo('Persistence on')
    else:
        echo('Persistence off')


@command()
def xdomenu():
    """interacts with a simple menu."""
    xmc = Command('xmctl')
    char_to_bin = {'q': ('srmenu'),
                   'c': ('clipmenu'),
                   'j': ('jmenu'),
                   'n': ('nvim'),
                   'h': ('htop'),
                   'u': ('myterm'),
                   'i': ('ipython'),
                   'p': ('perl'),
                   'r': ('ranger'),
                   'a': ('allpads'),
                   'P': ('pomodoro')}
    xdo = Command('xdotool')
    hinter = EWMH()
    persistent = False
    print_menu(persistent)
    while True:
        char = getchar()
        try:
            (opts) = char_to_bin[char]
            if persistent:
                xmc('minone')
            else:
                xmc('copykill')
            xmc(opts)
        except (KeyError):
            if char == '\t':
                persistent = not persistent
                print_menu(persistent)
                continue
            elif char == ' ':
                xmc('nextempty')
                continue
            if char == 'b':
                if persistent:
                    xmc('minone')
                else:
                    xmc('copykill')
                vis = class_is_visible(hinter, 'urxv')
                if vis is None:
                    xmc('byobu')
                    sleep(1)
                elif vis:
                    xmc('sendbyo')
                else:
                    xmc('bringbyo')
        sleep(0.5)
        if persistent:
            xmc('rest')
            continue
        xdo(['key', 'Menu'])
