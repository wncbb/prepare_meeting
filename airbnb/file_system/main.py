import collections

class FileSystem:
    def __init__(self):
        self.fileMap=collections.defaultdict()
        self.callbackMap=collections.defaultdict()
        self.fileMap[""]=0

    def create(self, filePath, value):
        if filePath in self.fileMap:
            return False
        lastSlashIndex=filePath.rindex('/')
        if filePath[:lastSlashIndex] not in self.fileMap:
            return False
        self.fileMap[filePath]=value
        return True
    
    def get(self, filePath):
        if filePath in self.fileMap:
            return self.fileMap[filePath]
        return -1

    def set(self, filePath, value):
        if filePath not in self.fileMap:
            return False
        self.fileMap[filePath]=value
        curPath=filePath
        while len(curPath)>0:
            if curPath in self.callbackMap:
                self.callbackMap[curPath]()
            lastSlashIndex=curPath.rindex('/')
            curPath=curPath[0:lastSlashIndex]
        return True

    def watch(self, filePath, callback):
        if filePath not in self.fileMap:
            return False
        self.callbackMap[filePath]=callback
        return True
    
s=FileSystem()
s.create('/a', 2)
print 'fileMap', s.fileMap
s.create('/a/b', 1)
print 'fileMap', s.fileMap
def tmp():
    print 'this is tmp'
s.watch('/a/b', tmp)
s.set('/a/b', 12)
print s.get('/a/b')