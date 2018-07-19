import unittest
import os
import time

from dvik_logging import dvik_logging as dvl


class TestGetHandler(unittest.TestCase):
    def setUp(self):
        curr_time = int(time.time())
        self.log_file = os.path.abspath('test{}.log'.format(curr_time))
        self.log_file_classic = os.path.abspath('test1{}.log'.format(curr_time))
        self.log_file_short = os.path.abspath('test2{}.log'.format(curr_time))
        self.log_file_no_time = os.path.abspath('test3{}.log'.format(curr_time))

        self.line_format_key_classic = 'classic'
        self.line_format_key_short = 'short'
        self.line_format_key_no_time = 'no_time'
        self.classic_line_format = dvl._LINE_FORMATS[self.line_format_key_classic]
        self.short_line_format = dvl._LINE_FORMATS[self.line_format_key_short]
        self.no_time_line_format = dvl._LINE_FORMATS[self.line_format_key_no_time]

        # default
        self.fh = dvl._get_file_handler(self.log_file)
        self.ch = dvl._get_console_handler()
        # classic
        self.classic_fh = dvl._get_file_handler(self.log_file_classic, line_format=self.line_format_key_classic)
        self.classic_ch = dvl._get_console_handler(line_format=self.line_format_key_classic)
        # short
        self.short_fh = dvl._get_file_handler(self.log_file_short, line_format=self.line_format_key_short)
        self.short_ch = dvl._get_console_handler(line_format=self.line_format_key_short)
        # no time
        self.no_time_fh = dvl._get_file_handler(self.log_file_no_time, line_format=self.line_format_key_no_time)
        self.no_time_ch = dvl._get_console_handler(line_format=self.line_format_key_no_time)

    def test_log_files_exist(self):
        self.assertTrue(os.path.exists(self.log_file))
        self.assertTrue(os.path.exists(self.log_file_classic))
        self.assertTrue(os.path.exists(self.log_file_short))
        self.assertTrue(os.path.exists(self.log_file_no_time))

    def test_get_file_handler(self):
        self.assertEqual(self.fh.formatter._fmt, self.classic_line_format)
        self.assertEqual(self.classic_fh.formatter._fmt, self.classic_line_format)
        self.assertEqual(self.short_fh.formatter._fmt, self.short_line_format)
        self.assertEqual(self.no_time_fh.formatter._fmt, self.no_time_line_format)

    def test_get_console_handler(self):
        self.assertEqual(self.ch.formatter._fmt, self.classic_line_format)
        self.assertEqual(self.classic_ch.formatter._fmt, self.classic_line_format)
        self.assertEqual(self.short_ch.formatter._fmt, self.short_line_format)
        self.assertEqual(self.no_time_ch.formatter._fmt, self.no_time_line_format)

    def tearDown(self):
        # zamykam kolejne loggery
        self.fh.flush()
        self.fh.close()
        self.classic_fh.flush()
        self.classic_fh.close()
        self.short_fh.flush()
        self.short_fh.close()
        self.no_time_fh.flush()
        self.no_time_fh.close()
        # usuwam pliki logów
        os.remove(self.log_file)
        os.remove(self.log_file_classic)
        os.remove(self.log_file_short)
        os.remove(self.log_file_no_time)


class TestCreation(unittest.TestCase):
    def setUp(self):
        self.base_path = os.path.abspath(os.path.dirname(__file__))

        self.logger_a = dvl.get_logger('a')
        self.logger_aa = dvl.get_logger('a')

        self.logger_b = dvl.get_logger('b')
        self.logger_bb = dvl.get_logger('b')

        self.logger_c = dvl.get_logger('c', ch_params={})
        self.logger_cc = dvl.get_logger('c')

        self.d_log_file_path = os.path.join(self.base_path, 'tmp_d.log')
        self.logger_d = dvl.get_logger('d', ch_params={})
        dvl.add_file_handler('d', file_path=self.d_log_file_path)
        self.logger_dd = dvl.get_logger('d', ch_params={'line_format': 'short'})

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
        dvl.clear_handlers('a')
        dvl.clear_handlers('b')
        dvl.clear_handlers('c')
        dvl.clear_handlers('d')

        os.remove(self.d_log_file_path)
        other_files = filter(lambda f_name: f_name.startswith('tmp_') and f_name.endswith('.log'),
                             os.listdir(self.base_path))
        for f_path in map(lambda f_name: os.path.join(self.base_path, f_name), other_files):
            os.remove(f_path)


class TestLogging(unittest.TestCase):
    def setUp(self):
        self.log_file = os.path.abspath('test.log')
        self.logger = dvl.get_logger('testlogger', ch_params={})
        dvl.add_file_handler('testlogger', file_path=self.log_file)

    def test_content(self):
        msg1 = 'jakaś wiadomość 1'
        msg2 = 'some other message'
        self.logger.info(msg1)
        self.logger.warning(msg2)
        with open(self.log_file, 'r') as fp:
            lines = fp.read().splitlines()
        self.assertIn(msg1, lines[-2])
        self.assertIn(msg2, lines[-1])

    def test_debug(self):
        msg = 'wiadomość debugująca'
        self.logger.debug(msg)
        with open(self.log_file, 'r') as fp:
            lines = fp.read().splitlines()
        if lines:
            self.assertNotIn(msg, lines[-1])

    def tearDown(self):
        dvl.clear_handlers('testlogger')
        os.remove(self.log_file)
