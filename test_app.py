from app import process_order

def test_process_order():
    assert process_order("1001") == "Processing Order 1001"
