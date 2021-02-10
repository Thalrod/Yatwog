from OpenGL.GL import *
from ctypes import *


class Loader:
    def __init__(self):
        self.vaos = []
        self.vbos = []
        pass

    def loadToVao(self, positions, indices):
        vaoID = self.createVao()
        self.bindIndicesBuffer(indices)
        self.storeDataInAttributeList(0, 3, positions)
        self.unbindVAO()
        return None

    def createVao(self):
        vaoID = glGenVertexArrays(1)
        self.vaos.append(vaoID)
        glBindVertexArray(vaoID)
        return vaoID

    def cleanup(self):
        for vao in self.vaos:
            glDeleteVertexArrays(vao)

        for vbo in self.vbos:
            glDeleteBuffers(vbo)

    def bindIndicesBuffer(self, indices):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboID)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * 4, (c_int * len(indices))(*indices), GL_STATIC_DRAW)

    def storeDataInAttributeList(self, attributeNumber, coordinateSize, data):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ARRAY_BUFFER, vboID)
        glBufferData(GL_ARRAY_BUFFER, len(data)*4, (c_float * len(data))(*data), GL_STATIC_DRAW)
        glVertexAttribPointer(attributeNumber, coordinateSize, GL_FLOAT, False, 0, 0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def unbindVAO(self):

        glBindVertexArray(0)
