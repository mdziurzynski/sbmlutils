"""
Test the SBML report.
"""
from __future__ import print_function, division
import unittest

import libsbml
import tempfile
from sbmlutils.examples import testfiles
from sbmlutils.report import sbmlreport
import os

class MyTestCase(unittest.TestCase):

    def test_demo_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(testfiles.demo_sbml, tmpdir)

    def test_galactose_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(testfiles.galactose_singlecell_sbml, tmpdir)

    def test_glucose_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(testfiles.glucose_sbml, tmpdir)

    def test_test_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(testfiles.small_sbml, tmpdir)

    def test_vdp_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(testfiles.vdp_sbml, tmpdir)

    def test_triggers_report(self):
        tmpdir = tempfile.mkdtemp(suffix="_sbml_report")
        sbmlreport.create_sbml_report(os.path.join(testfiles.test_dir, "models", "cubicSpline.xml"), tmpdir)

if __name__ == '__main__':
    unittest.main()