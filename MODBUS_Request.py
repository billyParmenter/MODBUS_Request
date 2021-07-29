import requests

inverter_address = 'http://192.168.1.31:502'

def Send_request_to_device(address, request):
    response = requests.post(address, request)
    return response


# Will read 122 registers starting at address 40001
# Tx: 01 03 9C 40 00 7A EB AD
#       byte[0] = Unit id to send request to
#       byte[1] = The function to perform 3 = read holding registers
#       byte[2:3] = The register address to start reading (40001)
#       byte[4] = The register amoutn / size of data
#           register 40000 will have least significant bytes
#           register 40001 will have most significant bytes

# Rx: 01 03 9C 40 00 XX XX
#       byte[0] = Unit id to send request to
#       byte[1] = The function to perform 3 = read holding registers
#       byte[2:3] = The register address to read (40001)
#       byte[4:7] = The register data
#       byte[4:5] = Least significant bytes
#       byte[6:7] = Most significant bytes
def Read_device_register(self, device_address):
    read_register_request = bytes.fromhex('01 03 9C 40 00 02')
    response = self.Send_request(device_address, read_register_request)
    print(response)


Read_device_register(inverter_address)