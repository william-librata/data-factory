#!./venv/bin/python

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener


channel_name = 'pubnub-market-orders'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-4377ab04-f100-11e3-bffd-02ee2ddab7fe'
pnconfig.ssl = False

pubnub = PubNub(pnconfig)

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels(channel_name).execute()
my_listener.wait_for_connect()
print('connected')

counter = 1
while(counter < 100):
    print(my_listener.wait_for_message_on(channel_name).message)
    counter += 1

pubnub.unsubscribe()
print('unsubscribed')
