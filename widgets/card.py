from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_file("widgets/card.kv")

class JournalEntryCard(MDCard):
    title = StringProperty()