
class ProgressBarUtil(object):
    def __init__(self, list, progress_bar) -> None:
        self.progress_bar = progress_bar

        self.iter = iter(list)
        self.max = len(list)
        self.val = 0

        self.progress_bar.setValue(0)

    def __iter__(self):
        return self
    
    def __next__(self):
        self.val += 1
        self.progress_bar.setValue(self.val/self.max * 100)

        if self.val > self.max:
            raise StopIteration()

        
        return self.iter.__next__()
