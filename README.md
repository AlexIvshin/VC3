Компиляция синтезатора голоса.\
https://github.com/RHVoice/RHVoice/blob/master/doc/ru/Compiling-on-Linux.md

После установки пакета vosk (pip install vosk):
необходимо скачать архив с русскоязычной моделью "vosk-model-small-ru-0.22".\
https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip   \
И разархивировать его в корневую папку проекта.

**opencv-python** не работает с numpy2!\
Необходимо понизить numpy2 до numpy1:\
pip uninstall numpy         \
pip install "numpy<2.0"