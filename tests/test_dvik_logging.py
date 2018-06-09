import unittest
import os
import time

import dvik_logging as dvl


class TestCreation(unittest.TestCase):
    def setUp(self):
        self.base_path = os.path.abspath(os.path.dirname(__file__))

        self.logger_a = dvl.get_logger('a')
        self.logger_aa = dvl.get_logger('a')

        self.logger_b = dvl.get_logger('b')
        self.logger_bb = dvl.get_logger('b')

        self.logger_c_console_handler = dvl.get_console_handler()
        self.logger_c = dvl.get_logger('c', console_handler=self.logger_c_console_handler)
        self.logger_cc = dvl.get_logger('c')

        self.logger_d_console_handler = dvl.get_console_handler()
        self.logger_dd_console_handler = dvl.get_console_handler(formatter=dvl.FORMATTERS.SHORT)
        self.d_log_file_path = os.path.join(self.base_path, 'tmp_d_{}.log'.format(int(time.time())))
        self.logger_d_file_handler = dvl.get_file_handler(log_file_path=self.d_log_file_path)
        self.logger_d = dvl.get_logger('d', console_handler=self.logger_d_console_handler,
                                       file_handler=self.logger_d_file_handler)
        self.logger_dd = dvl.get_logger('d', console_handler=self.logger_dd_console_handler)

    def test_creation_a(self):
        self.assertIs(self.logger_a, self.logger_aa)
        self.assertIsNot(self.logger_a, self.logger_b)
        self.assertIsNot(self.logger_aa, self.logger_c)
        self.assertIsNot(self.logger_a, self.logger_dd)

    def test_creation_b(self):
        self.assertIs(self.logger_b, self.logger_bb)
        self.assertIsNot(self.logger_bb, self.logger_a)
        self.assertIsNot(self.logger_b, self.logger_c)
        self.assertIsNot(self.logger_b, self.logger_dd)

    def test_creation_c(self):
        pass

    def test_creation_d(self):
        pass

    def tearDown(self):
        self.logger_d_file_handler.flush()
        self.logger_d_file_handler.close()

        os.remove(self.d_log_file_path)
        other_files = filter(lambda f_name: f_name.startswith('tmp_') and f_name.endswith('.log'),
                             os.listdir(self.base_path))
        for f_path in map(lambda f_name: os.path.join(self.base_path, f_name), other_files):
            os.remove(f_path)
