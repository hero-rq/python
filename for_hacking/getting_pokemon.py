import base64

message = "nimda"

for i in range(20):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    message = base64_message

print(base64_message)
