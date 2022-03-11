import math as maths
from pydub import AudioSegment
from noise import pnoise2

class beatmaker:
    def __init__(self, repeatTimes, sequenceLength, beatsInBar, weights = None):
        if not weights:
            weights = [abs((i / beatsInBar) - (beatsInBar / 2)) for i in range(sequenceLength)]
        self.repeatTimes = repeatTimes
        self.sequenceLength = sequenceLength
        self.beatsInBar = beatsInBar
        self.weights = weights
        self.result = []
    
    def getNoise(self, n):
        return [pnoise2(
            x,
            n,

        ) for x in range(self.sequenceLength)]
    
    def generate(self):
        output = []
        sequence = self.weights
        for i in range(self.repeatTimes):
            noise = self.getNoise(i)
            for beat in range(len(sequence)):
                sequence[beat] += noise[beat]
            output.append(sequence)
        self.output = output
    
    def render(self, sample, noisePathOut, bpm=120):
        clip = AudioSegment.silent(self.repeatTimes * self.sequenceLength * self.beatsInBar * 1000)
        sound = AudioSegment.from_file(sample, sample.split(".")[-1])
        for bar in range(self.output):
            for beat in range(bar):
                if (beat > 0):
                    clip.overlay(sound, position = )