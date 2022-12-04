from theatre import theatre


if __name__ == "__main__":
    from act_main import Act_Main
    theatre.current_act = Act_Main()

    theatre.Begin()