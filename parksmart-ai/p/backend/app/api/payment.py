from fastapi import APIRouter
router = APIRouter()

@router.post("/create-payment")
def create_payment(amount: float):
    return {"status": "created", "amount": amount, "payment_id": "pay_test_123"}
