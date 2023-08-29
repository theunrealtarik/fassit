
import os
import pyautogui
import ttkbootstrap as UI

WIN_WIDTH = 280
WIN_HEIGHT = 120
BTN_IMG_PATH = os.path.join(os.getcwd(), "assets", "accept.png")


class Main(UI.Window):
    def __init__(self):
        super().__init__(title="FASSIT", themename="darkly")
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.resizable(False, False)
        self.iconbitmap(os.path.join(
            os.getcwd(), "assets", "icons", "ico.ico"))
        self.feedback_text = UI.StringVar()
        self.feedback_text.set("waiting to see accept button ... 👀")

        if not os.path.exists(BTN_IMG_PATH):
            self.feedback_text.set("accept image sample was not found 😆")

        UI.Label(master=self, textvariable=self.feedback_text,
                 anchor="center", justify="center", font="Arial 12").pack(fill="both", expand=True)

    def invoke(self):
        btn_region = pyautogui.locateOnScreen(
            BTN_IMG_PATH, confidence=0.9, minSearchTime=5)

        if btn_region != None:
            (btnX, btnY) = (btn_region.left + (btn_region.width) /
                            2, btn_region.top + (btn_region.height)/2)
            pyautogui.moveTo(btnX, btnY)
            pyautogui.click(btnX, btnY)
        else:
            pass

        self.after(1000, self.invoke)


if __name__ == "__main__":
    try:
        main_window = Main()
        main_window.after(2000, main_window.invoke)
        main_window.mainloop()
    except KeyboardInterrupt:
        exit(1)
