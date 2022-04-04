
class ProgressBarUtil(object):
    def __init__(self, list, progress_bar) -> None:
        self.progress_bar = progress_bar

        self.list = list
        self.index = -1

        self.progress_bar.setValue(0)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        self.progress_bar.setValue((self.index + 1)/len(self.list) * 100)

        if self.index >= len(self.list):
            self.index = -1 # reset index
            raise StopIteration()

        
        return self.list[self.index]
