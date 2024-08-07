"""
Notify
  https://github.com/ms7m/notify-py
"""



from notifypy import Notify


if __name__ == "__main__":
  notification = Notify()
  notification.title = "Cool Title"
  notification.message = "Even cooler message."
  notification.send()


