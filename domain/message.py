class message_data:
    device_id = ""
    message = ""

    def get_Data(self):

        return {
            "deviceID": self.device_id,
            "message": self.message
        }