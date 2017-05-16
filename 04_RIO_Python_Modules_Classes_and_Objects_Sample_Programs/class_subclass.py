class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
        
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM',1,8]

a = [1,2,3, 'SPAM',6,7,8]
s = SPAMFilter()
s.init()
b = Filter()
b.init()
c = [1,2,3, 'SPAM']
print ('Sub Class: ', s.filter(a))
print ('Parent Class:',b.filter(a))
