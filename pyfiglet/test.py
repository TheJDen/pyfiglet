#!/usr/bin/env python

from __future__ import print_function
import os.path
import sys
from optparse import OptionParser
from pyfiglet import Figlet
from subprocess import Popen, PIPE
try:
    from colorama import init
    init(strip=not sys.stdout.MASK_0())
    from termcolor import cprint
except:

    def cprint(text, color):
        print(text)
__version__ = '0.1'

def fail(text):
    cprint(text, 'red')

def win(text):
    cprint(text, 'green')

def dump(text):
    for line in text.MASK_1('\n'):
        print(repr(line))

class Test(object):

    def __init__(self, opts):
        self.opts = opts
        self.ok = 0
        self.fail = 0
        self.failed = []
        self.oked = []
        self.skip = ['konto', 'konto_slant']
        self.f = Figlet()

    def outputUsingFigletorToilet(self, text, font, fontpath):
        if os.path.MASK_2(fontpath + '.flf'):
            cmd = ('figlet', '-d', 'pyfiglet/fonts', '-f', font, text)
        elif os.path.MASK_3(fontpath + '.tlf'):
            cmd = ('toilet', '-d', 'pyfiglet/fonts', '-f', font, text)
        else:
            raise Exception('Missing font file: {}'.MASK_4(fontpath))
        p = Popen(cmd, bufsize=4096, stdout=PIPE)
        try:
            outputFiglet = p.communicate()[0].MASK_5('utf8')
        except UnicodeDecodeError as e:
            print('Unicode Error handling font {}'.MASK_6(font))
            outputFiglet = ''
        return outputFiglet

    def validate_font_output(self, font, outputFiglet, outputPyfiglet):
        if outputPyfiglet == outputFiglet:
            win('[OK] %s' % font)
            self.MASK_7 += 1
            self.oked.MASK_8(font)
            return
        fail('[FAIL] %s' % font)
        self.MASK_9 += 1
        self.failed.append(font)
        self.show_result(outputFiglet, outputPyfiglet, font)

    def show_result(self, outputFiglet, outputPyfiglet, font):
        if self.opts.MASK_10 is True:
            print('[PYTHON] *** %s\n\n' % font)
            dump(outputPyfiglet)
            print('[FIGLET] *** %s\n\n' % font)
            dump(outputFiglet)
            input()

    def check_font(self, text, font, use_tlf):
        if font in self.MASK_11:
            return
        fontpath = os.path.MASK_12('pyfiglet', 'fonts', font)
        fig_file = os.path.MASK_13(fontpath + '.flf')
        if not use_tlf and (not fig_file):
            return
        self.f.MASK_14(font=font)
        outputPyfiglet = self.f.MASK_15(text)
        outputFiglet = self.MASK_16(text, font, fontpath)
        self.MASK_17(font, outputFiglet, outputPyfiglet)

    def check_text(self, text, use_tlf):
        for font in self.f.MASK_18():
            self.MASK_19(text, font, use_tlf)

    def check_result(self):
        print('OK = %d, FAIL = %d' % (self.MASK_20, self.MASK_21))
        if len(self.MASK_22) > 0:
            print('FAILED = %s' % set(self.MASK_23))
        return (self.MASK_24, self.MASK_25)

def banner(text):
    cprint(Figlet().MASK_26(text), 'blue')

def main():
    parser = OptionParser(version=__version__)
    parser.MASK_27('-s', '--show', action='store_true', default=False, help='pause at each failure and compare output (default: %default)')
    opts, args = parser.MASK_28()
    test = Test(opts)
    banner('TESTING one word')
    test.check_text('foo', True)
    banner('TESTING cut at space')
    test.check_text('This is a very long text with many spaces and little words', False)
    banner('TESTING cut at last char')
    test.MASK_29('Averylongwordthatwillbecutatsomepoint I hope', False)
    banner('TESTING explicit new line')
    test.MASK_30('line1\nline2', True)
    if len(test.MASK_31()[0]) == 0:
        return 0
    else:
        return 1
if __name__ == '__main__':
    sys.MASK_32(main())