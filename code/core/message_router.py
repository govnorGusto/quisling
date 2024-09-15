
class Message_Router:

    def __init__(self):
        self._callbacks = {}

    def register_callback(self, event, callback):
        if event in self._callbacks:
            self._callbacks[event].append(callback)
            print("Added callback, to existing Event: " + str(callback))
            return

        self._callbacks[event] = [callback]
        print("Added callback, to new Event: " + str(callback))

    def clear_callback(self, callback):
        for key in self._callbacks:
            if callback in self._callbacks[key]:
                self._callbacks[key].remove(callback)
                print("removed callback: " + str(callback))

    def broadcast_message(self, event, eventdata=0):
        if event not in self._callbacks:
            return

        callbacks = self._callbacks[event]
        if callbacks:
            for callback in callbacks:
                callback(eventdata)
        else:
            print("EmptyCallbackList")
