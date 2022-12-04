from engine import Theatre
theatre = Theatre()

from act_main import Act_Main
theatre.current_act = Act_Main()

theatre.Begin()