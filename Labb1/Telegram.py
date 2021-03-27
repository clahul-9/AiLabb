class Telegram():
    def __init__(self,sender,reciver,msg,dispatchTime, extraInfo):
        self.sender = sender
        self.reciver = reciver
        self.msg = msg
        self.dispatchTime = dispatchTime
        self.extaInfo = extraInfo