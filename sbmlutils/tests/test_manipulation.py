import unittest

import libsbml
import os
from sbmlutils import comp
from sbmlutils import manipulation
from sbmlutils import validation


class MyTestCase(unittest.TestCase):

    def test_biomodel_merge(self):
        from os.path import join as pjoin
        from sbmlutils.tests.resources import resources_dir

        manipulation_dir = pjoin(resources_dir, 'manipulation')
        cur_dir = os.getcwd()
        os.chdir(manipulation_dir)

        # dictionary of ids & paths of models which should be combined
        # here we just bring together the first Biomodels
        model_ids = ["BIOMD000000000{}".format(k) for k in range(1, 5)]
        model_paths = dict(zip(model_ids, ["{}.xml".format(mid) for mid in model_ids]))
        print(model_paths)

        # merge model
        doc = manipulation.merge_models(model_paths, validate=False)
        self.assertIsNotNone(doc)
        Nall, Nerr, Nwarn = validation.check_doc(doc, ucheck=False)
        self.assertEqual(Nerr, 0)
        self.assertEqual(Nwarn, 0)
        self.assertEqual(Nall, 0)

        # flatten the model
        doc_flat = comp.flattenSBMLDocument(doc)
        self.assertIsNotNone(doc_flat)
        Nall, Nerr, Nwarn = validation.check_doc(doc_flat, ucheck=False)
        self.assertEqual(Nerr, 0)
        self.assertEqual(Nwarn, 0)
        self.assertEqual(Nall, 0)

        os.chdir(cur_dir)


if __name__ == '__main__':
    unittest.main()
