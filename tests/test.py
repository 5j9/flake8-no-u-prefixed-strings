from subprocess import Popen, PIPE
from unittest import TestCase, main


expected_output = '''\
test_case.py:4:10: U001: u-prefixed string u\'\'\'\\nNO\\n\'\'\'
test_case.py:10:12: U001: u-prefixed string u'a'
test_case.py:12:12: U001: u-prefixed string U'a'
test_case.py:13:12: U001: u-prefixed string u"b"
test_case.py:14:12: U001: u-prefixed string u"b"
test_case.py:16:12: U001: u-prefixed string u"""c"""
'''


class PluginTest(TestCase):

    """Test the plugin."""

    def test_plugin(self):
        """Run the plugin on test_case.py."""
        # Fist see that the plugin actually exists
        popen = Popen(
            args=['python', '-m', 'flake8', '--version'],
            stdout=PIPE,
            universal_newlines=True,
        )
        stdout_data, stderr_data = popen.communicate()
        assert stderr_data is None
        self.assertIn(
            'flake8-no-u-prefixed-string',
            stdout_data,
            'flake8-no-u-prefixed-string is not installed',
        )
        popen = Popen(
            args=[
                'python', '-m', 'flake8', '--select=U001',
                '--ignore=H,E,D,N,F', 'test_case.py'
            ],
            stdout=PIPE,
            universal_newlines=True,
        )
        stdout_data, stderr_data = popen.communicate()
        assert stderr_data is None
        print(stdout_data)
        self.assertEqual(
            stdout_data,
            expected_output,
        )


if __name__ == '__main__':
    main()
