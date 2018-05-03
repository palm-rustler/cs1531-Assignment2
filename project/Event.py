class Event(object):
    def __init__(self, title, status, type_, convener, venue, capacity, start_date, end_date):
        self.title = title
        self.status = status
        self.type = type_
        self.convener = convener
        self.venue = venue
        self.capacity = capacity
        self.start_date = start_date
        self.end_date = end_date
    def create_event(self):
        pass
    def register_user(self):
        pass
    def deregister_user(self):
        pass
    def alter_event(self):
        pass
    def get_event(self)
        pass
class Course(Event):
    def __init__(self):
        super().__init__(self,title, status, type_, convener, venue, capacity, start_date, end_date)
        self.session_list = []
    def add_session(self, new_session)
        self.session_list.append(new_session)
class Seminars(Event):
    def __init__(self):
        self.session_list = []
    def add_session(self, new_session)
        self.session_list.append(new_session)
class Session(Seminars):
    def __init__(self):
        self.title = title
        self.presenter = presenter
        self.date = date
        self.time = []
    def new_session(self):
        pass
    def change_session(self):
        pass
    
    
