from fastapi import HTTPException, APIRouter, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from config import async_session
from dal.user import UserDAL
from model.user import User as UserModel

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_username(form_data.username) if hasattr(user_dal, 'get_user_by_username') else None
            if not user or not user.verify_password(form_data.password):
                raise HTTPException(
                    status_code=400,
                    detail="Incorrect username or password"
                )
            # TODO: Create Session token and return it
            return {"access_token": "ADD TOKEN HERE", "token_type": "bearer"}

@router.post("/register")
async def register(user: UserModel):
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            created = await user_dal.create(user)
            return created.__dict__

@router.post("/logout")
async def logout(authorization: str = Header(None)):
    # TODO: Impl
    pass