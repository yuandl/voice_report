import datetime
from kdxf.iat_ws_python3 import *
from audio_tool.pyaudio_util import *

if __name__ == "__main__":
    filename = "test"

    print("-------start----------")
    print(datetime.datetime.now())
    # filename = audio_record(filename)

    # audio2text(filename + ".pcm")
    # result = audio2text("test_1.pcm")  # 床前明月光，疑是地上霜，举头望明月，低头思故乡
    # print(datetime.datetime.now())
    # print(result)

    result = "床前明月光，疑是地上霜，举头望明月，低头思故乡。"
