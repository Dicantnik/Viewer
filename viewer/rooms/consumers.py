import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['code']
        self.room_group_name = f'room_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
            )
        
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json['type'])
        if text_data_json['type'] == 'message':
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type': 'chat_message',
                    'message': text_data_json['message'],
                    'sender': text_data_json['sender'],
                }
            )
        elif text_data_json['type'] == 'video':
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type': 'video_message',
                    'message': text_data_json['message'],
                    'time': text_data_json['time'],
                }
            )

        # elif text_data_json['type'] == 'video':


    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
                    'type': 'message',
                    'message': event['message'],
                    'sender': event['sender'],

        })) 

    
    async def video_message(self, event):
        await self.send(text_data=json.dumps({
                    'type': 'video',
                    'message': event['message'],
                    'time': event['time'],
        })) 

