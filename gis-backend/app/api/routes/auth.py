from fastapi import APIRouter, Depends, HTTPException
from app.auth.schemas import LoginRequest, LoginResponse, UserInfo
from app.auth.auth import create_access_token, verify_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Dummy login route (replace with real DB logic)
@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    # This is mock logic – in real apps, check hashed password from DB
    if request.email == "admin@example.com" and request.password == "admin123":
        token = create_access_token({"sub": request.email, "role": "Admin"})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Return decoded token info
@router.get("/me", response_model=UserInfo)
def get_me(user: dict = Depends(verify_token)):
    return user
