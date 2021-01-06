from faker.providers import BaseProvider


class Provider(BaseProvider):
    greetings = (
        'Greetings! What can I do for you today?',
        'Hello and Welcome. How can I assist you today?',
        'Hello and welcome, what would you like me to do for you?',
        'Hello there. What brings you here today?',
        'Hello! Can I help you with something?',
        'Hello! Can I help you?',
        'Hello! How might I help you today?',
        'Hello, how can I help you?',
        'Hello, how may I assist you?',
        'Hello, how may I help you today?',
        'Hello, what can I help you with today?',
        'Hello, what could I help you with?',
        'Hello, what seems to be the issue?',
        'Hello. How can I help you today?',
        'Hello. How can I help you?',
        'Hey there, what seems to be the issue?',
        'Hi there, what brings you here?',
        'Hi! What can I help you with today?',
        'Hi, how can I help you?',
        'Hi, what could I do for you?',
        'Hi, what do you need help with today?',
        'Hi. How can I help you today?',
        'How can I assist you today?',
        'How can I be of assistance?',
        'How can I be of service?',
        'How may I assist you?',
        'Is there anything I can do for you today?',
        'Welcome! How can I help you out today?',
        'Welcome! How may I be of assistance?',
        'Welcome, how can I help you?',
        'Welcome, what can I do for you?',
        'Welcome. How can I assist you today?',
        'Welcome. How can I help you?',
        'Welcome. How may I help you?',
        'Welcome. What can I do for you today?',
        'Welcome. What can I do for you?',
        'What can I do for you today?',
        'What can I do for you?',
        'What can I do to help you today?',
        'What can I do to help you?',
        'What can I do to help?',
        'What can I help you with today?',
        'What can I help you with?',
        'What may I assist you with today?'
    )

    def greeting(self):
        return self.random_element(self.greetings)
