from twilio.rest import Client

account_sid = 'AC435f4663d49c7dccb2e8624f2077e219'
auth_token = 'eea07558f098a05da15b2e64a8b506dd'
client = Client(account_sid, auth_token)
numbers = ['+917891493322', '+917370935441', '+918005966488']
for i in numbers:
    message = client.messages.create(
                              from_='+17543001302',
                              body='Hey Frideler, You got an Order. Check On https://fridel.in/',
                              to=i
                          )

# message_pankaj = client.messages.create(
#                               from_='+17543001302',
#                               body='Hey Frideler, You got an Order. Check On https://fridel.in/',
#                               to='+917370935441'
#                           )
#
# message_yash = client.messages.create(
#                               from_='+17543001302',
#                               body='Hey Frideler, You got an Order. Check On https://fridel.in/',
#                               to='+918005966488'
#                           )
