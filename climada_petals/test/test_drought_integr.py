"""
This file is part of CLIMADA.

Copyright (C) 2017 ETH Zurich, CLIMADA contributors listed in AUTHORS.

CLIMADA is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free
Software Foundation, version 3.

CLIMADA is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with CLIMADA. If not, see <https://www.gnu.org/licenses/>.

---

Tests on Drought Hazard exposure and Impact function.
"""

import unittest

from climada_petals.hazard.drought import Drought
from climada.engine import Impact
from climada_petals.entity.exposures.spam_agrar import SpamAgrar
from climada.entity.impact_funcs import ImpactFuncSet
from climada_petals.entity.impact_funcs.drought import ImpfDrought


class TestIntegr(unittest.TestCase):
    """Test loading functions from the Drought class"""
    def test_switzerland(self):

        drought = Drought()
        drought.set_area(44.5, 5, 50, 12)

        hazard_set = drought.setup()

        imp_drought = Impact()
        dr_impf = ImpactFuncSet()
        impf_def = ImpfDrought.from_default()
        dr_impf.append(impf_def)

        exposure_agrar = SpamAgrar()
        exposure_agrar.init_spam_agrar(country='CHE', haz_type='DR')
        exposure_agrar.assign_centroids(hazard_set)
        imp_drought.calc(exposure_agrar, dr_impf, hazard_set)

        index_event_start = imp_drought.event_name.index('2003')
        damages_drought = imp_drought.at_event[index_event_start]

        self.assertEqual(hazard_set.haz_type, 'DR')
        self.assertEqual(hazard_set.size, 114)
        self.assertEqual(hazard_set.centroids.size, 130)
        self.assertEqual(exposure_agrar.latitude.size, 766 / 2)
        self.assertAlmostEqual(exposure_agrar.value[3], 1720024.4)
        self.assertAlmostEqual(damages_drought, 61995472.555223145)


# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestIntegr)
    unittest.TextTestRunner(verbosity=2).run(TESTS)
