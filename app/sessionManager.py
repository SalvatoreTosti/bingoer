from app.session import Session

class SessionManager():
    def __init__(self):
        self._sessions = []
        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        
    def close(self):
        pass
    
    @property
    def sessionNames(self):
        names = []
        for session in self._sessions:
            names.append(session.name)
        return names
    
    def createSession(self, name, mode, width, height, words):
        newSession = Session(name, mode, width, height, words)
        self._sessions.append(newSession)
        return newSession
    
    def fetchSession(self, name):
        for session in self._sessions:
            if session.name == name:
                return session
        return None