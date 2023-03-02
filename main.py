from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
#from pythonosc.osc_server import AsyncIOOSCUDPServer
import logging
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

logging.basicConfig(format='[{asctime}][{levelname[0]}] {message}', \
                    style='{', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
_l = logging.getLogger("vrc-osc-imm")
_l.debug("Set up formatting and level for log, establishing paths and function definition")
audio_segs = {"L": AudioSegment.from_mp3("./assets/audio/left.mp3"), "R": AudioSegment.from_mp3("./assets/audio/right.mp3")}
def play_clip(addr, val):
    _l.debug(f"{addr}:{val}")
    side = addr[-1]
    if val:
        if side not in ('L','R'):
            _l.error("OSC address not valid for audio playback")
        else:
            _l.info(f"Playing {side}")
            #play_file(audio_paths[side])
            play_obj = _play_with_simpleaudio(audio_segs[side])

_l.debug("Creating dispatcher and mapping OSC addresses")
dispatcher = Dispatcher()
dispatcher.map("/avatar/parameters/Touch_Ear_*",play_clip)
server_addr = ("127.0.0.1",9001)
#server = AsyncIOOSCUDPServer(server_addr, dispatcher, asyncio.get_event_loop())
server = ThreadingOSCUDPServer(server_addr, dispatcher)
_l.info(f"Starting server at {server_addr[0]}:{server_addr[1]}")
#server.serve()
server.serve_forever()
_l.info("Exiting")