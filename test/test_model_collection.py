from mhc2 import ModelCollection, Ensemble
from nose.tools import eq_

def test_new_model_collection_is_empty():
    mc = ModelCollection("_test")
    eq_(mc.alleles(), [])
    mc.delete()

def test_add_empty_ensemble():
    mc = ModelCollection("_test")
    e = Ensemble()
    mc.add_model("DRB1*01:01", e)
    mc.clear_cache()
    e2 = mc.get_model("DRB1*01:01")
    eq_(e, e2)