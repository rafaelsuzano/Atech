# -*- coding: utf-8 -*-
import CoreTest
import os
import unittest
import HtmlTestRunner

from pathlib import Path

current_directory = Path('\\report')
FP =  unittest.defaultTestLoader.loadTestsFromTestCase(CoreTest.FP)
suite = unittest.TestSuite([FP])

suite = unittest.TestSuite([suite])
html_runner = HtmlTestRunner.HTMLTestRunner(report_title='Atech Airlines', descriptions=u"Cenarios de teste",
                                         combine_reports=True, output=current_directory,
                                         add_timestamp=False,
                                         report_name="Projeto ATECH",
                                         failfast = False,
                                         buffer = True)


html_runner.run(suite)

if __name__ == '__main__':
    unittest.main()
