class Book:
    def __init__(self,id,availabel,title,timestamp):
        self.id=id
        self.title=title
        self.availabel=availabel
        self.timestamp=timestamp


        def __repr__(self):
            return '<id {}>'.format(self.id)
        

        def serialize(self):
            return{
                'id':self.id,
                'title':self.title,
                'availabel':self.avaialabel,
                'timestamp':self.timestamp
            }
