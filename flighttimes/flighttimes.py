'''check the flight times for dhl freight flights'''
from time import sleep
from bs4 import BeautifulSoup
from requests import Session, post
from requests.exceptions import (HTTPError, MissingSchema, InvalidURL)
from termcolor import colored
from click import command


def find_nc(tagl, tag):
    '''find the next class with given tag name tag'''
    return tagl.find_next(class_=tag)


def soup_t(soup_text):
    '''return the flight time given the html text or None if not en route'''
    b_tag = soup_text.body
    t_tag = find_nc(b_tag, "track-panel-actualtime")
    t_tag = find_nc(t_tag, "track-panel-actualtime")
    a_tags = find_nc(b_tag, "track-panel-arrival").a
    arrival = a_tags.text
    t_text = t_tag.text
    panel = find_nc(b_tag, "track-panel-inner")
    status = find_nc(panel, 'smallrow1')
    print('Arriving in ' + arrival + ' at ' + t_text)
    print(status.text)
    if "En Route" in status.text and 'KSLC' in arrival:
        return t_text
    else:
        return None


@command()
def text_loop():
    '''send messages when the flights are en route'''
    inbound_rno = ('http://flightaware.com/live/flight/SOO594', '594')
    inbound = ('http://flightaware.com/live/flight/SOO597', '597')
    night_boi = ('http://flightaware.com/live/flight/AMF1062', '1062')
    night_mhr = ('http://flightaware.com/live/flight/SOO197', '197')

    npyurl = "https://npy.hipchat.com/v2/room/2674348/notification"
    flights = (inbound_rno, inbound, night_boi, night_mhr)
    with Session() as ses:
        print('session has begun')
        while True:
            print(colored('------------------------', 'white'))
            for flight in flights:
                print('')
                try:
                    page = ses.get(flight[0])
                except InvalidURL:
                    print('invalid url, ' + flight[0])
                    break
                except MissingSchema:
                    print('add http')
                    break
                except HTTPError:
                    print('http error')
                    break
                soup_in = BeautifulSoup(page.text, 'html.parser')
                f_num = soup_in.title.string.split('#')[0] + flight[1]
                print(colored(f_num, 'yellow'))
                arr = soup_t(soup_in)
                if arr is None:
                    continue
                msg = f_num + ' arrives at ' + arr
                print(colored(msg, 'green'))
                token = "EkpHuaUe6GBYfXf9JFo32UqZ3GJ1AkHbiABr3r40"
                npydat = {
                    'auth_token': token,
                    'notify': 'false',
                    'message_format': 'text',
                    'message': msg}
                post(npyurl, data=npydat)
            sleep(300)
