import argparse
import os

import qi


def connect(ip: str, port: int = 9559) -> qi.Session:
    session = qi.Session()
    session.connect(f"tcp://{ip}:{port}")
    return session


def main() -> None:
    parser = argparse.ArgumentParser(prog="embodied")
    parser.add_argument("--ip", default=os.environ.get("NAO_IP", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("NAO_PORT", "9559")))
    parser.add_argument("--say", default="你好，我是 Embodied")
    args = parser.parse_args()

    session = connect(args.ip, args.port)
    tts = session.service("ALTextToSpeech")
    tts.setLanguage("Chinese")
    tts.say(args.say)
