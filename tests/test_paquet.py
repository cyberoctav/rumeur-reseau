def test_paquet_importable():
    """Le paquet s'importe : vérifie que le src layout et le pyproject sont corrects."""
    import rumeur_reseau

    assert rumeur_reseau.__name__ == "rumeur_reseau"