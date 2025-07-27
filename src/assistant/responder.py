class Responder:
    def __init__(self, voice_engine):
        self.voice_engine = voice_engine

    def respond(self, text):
        """Generate spoken responses."""
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def provide_feedback(self, feedback):
        """Give feedback to the user."""
        self.respond(feedback)