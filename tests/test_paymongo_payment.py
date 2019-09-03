import paymongo


def test_exec_create_payment():
    token = paymongo.Payment.create(None)
