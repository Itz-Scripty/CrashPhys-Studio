# ============================================================
# CrashPhys Studio
# File: main.py
# Version: 0.1.0
#
# Application launcher
# ============================================================


import moderngl_window as mglw

from engine.viewport import CrashViewport




def main():


    mglw.run_window_config(
        CrashViewport
    )




if __name__ == "__main__":

    main()