from collections import deque

class expenses:
    def __init__(self):
        self.total=0
        self.details={}
        self._history=deque()
    
    def add_detail(self, _month, **kwargs):
        self.details.clear()
        self.total=0
        for key, value in kwargs.items(): 
            self.details[key] = int(value)
            self.total += int(value)
        self._history.append({_month:(self.total, self.details)})
        if len(self._history)==7:
            temp=self._history.pop()

    def get_history(self):
        return list(self._history)

    

        


    

