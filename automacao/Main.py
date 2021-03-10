# -*- coding: utf-8 -*-
import CoreTest
import os
import unittest
import HtmlTestRunner




FP =  unittest.defaultTestLoader.loadTestsFromTestCase(CoreTest.FP)
suite = unittest.TestSuite([FP])

suite = unittest.TestSuite([suite])
html_runner = HtmlTestRunner.HTMLTestRunner(report_title='Atech Airlines', descriptions=u"Cenarios de teste",
                                         combine_reports=True, output="/var/lib/jenkins/workspace/Automacao/automacao",
                                         add_timestamp=False,
                                         report_name="ProjetoATECH",
                                         failfast = False,
                                         buffer = True)


html_runner.run(suite)

if __name__ == '__main__':
    unittest.main()
