def test_import_and_version():
    import RAJ1000_tester

    assert isinstance(RAJ1000_tester.__version__, str)
