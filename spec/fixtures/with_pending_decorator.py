from mamba import description, _it, _context

with description('Fixture#with_pending_decorator'):
    with _it(' pending_spec'):
        pass

    with _context('when pending context'):
        pass
