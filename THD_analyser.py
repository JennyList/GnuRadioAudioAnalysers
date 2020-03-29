#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: THD Analyser
# Author: Jenny List
# Description: A simple single-frequency THD analyser for audio work
# Generated: Sun Mar 29 17:25:52 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class THD_analyser(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "THD Analyser")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("THD Analyser")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "THD_analyser")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.frequency = frequency = 1000
        self.cut_off = cut_off = frequency/10
        self.transition_width = transition_width = cut_off/10
        self.samp_rate = samp_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, frequency+cut_off-transition_width, transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, frequency+cut_off+(transition_width*1.1), transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(32, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_rms_xx_0_0 = blocks.rms_ff(0.0001)
        self.blocks_rms_xx_0 = blocks.rms_ff(0.0001)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100, ))
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, frequency, 0.5, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.audio_sink_0, 1))
        self.connect((self.audio_source_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.audio_source_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.audio_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_rms_xx_0_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_rms_xx_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.dc_blocker_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "THD_analyser")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_cut_off(self.frequency/10)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.frequency+self.cut_off-self.transition_width, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.frequency+self.cut_off+(self.transition_width*1.1), self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.analog_sig_source_x_0.set_frequency(self.frequency)

    def get_cut_off(self):
        return self.cut_off

    def set_cut_off(self, cut_off):
        self.cut_off = cut_off
        self.set_transition_width(self.cut_off/10)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.frequency+self.cut_off-self.transition_width, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.frequency+self.cut_off+(self.transition_width*1.1), self.transition_width, firdes.WIN_BLACKMAN, 6.76))

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.frequency+self.cut_off-self.transition_width, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.frequency+self.cut_off+(self.transition_width*1.1), self.transition_width, firdes.WIN_BLACKMAN, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.frequency+self.cut_off-self.transition_width, self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.frequency+self.cut_off+(self.transition_width*1.1), self.transition_width, firdes.WIN_BLACKMAN, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=THD_analyser, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
