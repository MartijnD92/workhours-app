import rumps
import datetime

class WorkhoursApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Workhours",
            "start": "Start Timer",
            "pause": "Pause Timer",
            "continue": "Continue Timer",
            "stop": "Stop Timer",
            "break_message": "Time to leave! Workday is over.",
            "interval": 28_800,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.target_time = datetime.timedelta(seconds=self.config["interval"])
        self.set_up_menu()
        self.start_pause_button = rumps.MenuItem(
            title=self.config["start"], callback=self.start_timer
        )
        self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
        self.menu_counter = rumps.MenuItem(self.target_time)
        self.app.menu = [
            self.menu_counter,
            self.start_pause_button,
            self.stop_button,
        ]

    def set_up_menu(self):
        self.timer.stop()
        self.timer.count = 0
        self.app.icon = "./clock.icns"
        self.app.title = ""

    def on_tick(self, sender):
        time_passed = datetime.timedelta(seconds=sender.count)

        if time_passed > self.target_time:
            rumps.notification(
                title=self.config["app_name"],
                subtitle=self.config["break_message"],
                message="",
            )
            self.stop_timer()
            self.stop_button.set_callback(None)
        else:
            self.stop_button.set_callback(self.stop_timer)
            self.menu_counter.title = time_passed
        sender.count += 1

    def start_timer(self, sender):
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start"]:
                self.timer.count = 0
                self.timer.end = self.target_time
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()

    def stop_timer(self, sender):
        self.set_up_menu()
        self.stop_button.set_callback(None)
        self.start_pause_button.title = self.config["start"]
        self.menu_counter.title = self.target_time

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = WorkhoursApp()
    app.run()
