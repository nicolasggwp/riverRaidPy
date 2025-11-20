import os
import shutil
import sys

def desinstalar_jogo():
    pasta_do_jogo = os.path.dirname(os.path.abspath(__file__))
    shutil.rmtree(pasta_do_jogo)
    sys.exit()

