from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty,OptionProperty,ObjectProperty,ListProperty,BooleanProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
Window.keyboard_anim_args={'d':.2,'t':'in_out_expo'}
Window.softinput_mode='below_target'
Window.size=(350,540)
import time
Builder.load_file('chatscreen.kv')

class MySentLabel(MDLabel):
	pass

class MyReceivedLabel(MDLabel):
	pass

class MyBox(MDBoxLayout):
    '''A chat bubble for the chat screen messages.'''

    msg = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    isRead = OptionProperty('waiting', options=['read', 'delivered', 'waiting'])

class ChatPage(MDScreen):
	def sendMessage(self):
		
		senttime=time.localtime()
		now=time.strftime("%H:%M",senttime)
		self.newmessage=self.ids.sendmessage.text+'       '
		self.mytime=MDLabel(text=f'[i][size=10]{now}[/size][/i] \n\n',markup=True,halign='right',valign='bottom')
		self.sentmessage=MySentLabel(text=self.newmessage,halign='left',valign='middle') 
		self.ids.chatting.add_widget(self.sentmessage)
		self.ids.chatting.add_widget(self.mytime)
		self.ids.sendmessage.text=''

	def receiveMessage(self):
		receivetime=time.localtime()
		now=time.strftime("%H:%M",receivetime)
		t='    '
		self.newmessage=self.ids.sendmessage.text+t*2
		posi={'x':(len(self.newmessage)/27*.58 if len(self.newmessage)<27 and len(self.newmessage)>15 else dp(.58) if len(self.newmessage)>=27 else len(self.newmessage)/27*.53)}
		self.mytime=MDLabel(text=f'[i][size=10][color=#ffffff]{now}[/color][/size][/i] \n\n',pos_hint=posi,markup=True,valign='bottom')

		receivemessage=MyReceivedLabel(text=self.newmessage)	
		
		self.ids.chatting.add_widget(receivemessage)
		self.ids.chatting.add_widget(self.mytime)
		self.ids.sendmessage.text=''
	
class MyChat(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Teal'
		return ChatPage()

LabelBase.register(name='Roboto',fn_regular='Jefferies.otf')
if __name__ == '__main__':
	MyChat().run()