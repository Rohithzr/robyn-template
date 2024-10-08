from robyn import Robyn
from robyn.authentication import AuthenticationHandler, BearerGetter, Identity

# Create the Robyn app instance
app = Robyn(__file__)

class BasicAuthHandler(AuthenticationHandler):
  def authenticate(self, request):
      token = self.token_getter.get_token(request)
      if token == "valid":
          return Identity(claims={})
      return None

app.configure_authentication(BasicAuthHandler(token_getter=BearerGetter()))

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/health")
async def health():
    return {"status": "ok"}

@app.get("/auth/v1/login")
async def login(request):
    return {"status": "ok"}

@app.get("/auth/v1/logout")
async def logout(request):
    return {"status": "ok"}

@app.get("/auth/v1/callback")
async def callback(request):
    return {"status": "ok"}

@app.get("/auth/v1/profile", auth_required=True)
async def get_profile(request):
    return {"status": "ok"}

@app.post("/auth/v1/profile", auth_required=True)
async def get_profile(request):
    return {"status": "ok"}

@app.patch("/auth/v1/profile", auth_required=True)
async def update_profile(request):
    return {"status": "ok"}

app.start(port=8080, host="0.0.0.0") 