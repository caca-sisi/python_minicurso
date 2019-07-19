import numpy

from array import array
from time import sleep

import pygame
from pygame.mixer import Sound, get_init, pre_init

class Note(Sound):
    def __init__(self, frequency, volume=.5):
        self.frequency = frequency
        try:
            Sound.__init__(self, buffer=self.build_samples())
        except:
            pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples_square(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples


    def build_samples(self):
        sample_rate = pygame.mixer.get_init()[0]
        period = int(round(sample_rate / self.frequency))
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1

        def frame_value(i):
            return amplitude * numpy.sin(2.0 * numpy.pi * self.frequency * i / sample_rate)

        return numpy.array([frame_value(x) for x in range(0, period)]).astype(numpy.int16)

if __name__ == "__main__":
    pre_init(44100, -16, 1, 1024)
    pygame.init()
    La4=Note(440)
    Si4=Note(493.88)
    Do =Note(523.25)
    Re =Note(587.33)
    Mi =Note(659.25)
    Fa =Note(698.46)
    Sol=Note(783.99)
    La =Note(880)
    Si =Note(987.77)
    notas= [Do,Re,Mi,Fa,Fa,Fa,
    Do, Re, Do, Re, Re , Re,
    Do, Sol, Fa, Mi, Mi, Mi,
    Do, Re, Mi, Fa]

    for nota in notas:
        nota.play(100000,200)
        sleep(1)

    sleep(5)
