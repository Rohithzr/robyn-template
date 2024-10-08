def setup_auth_routes(app):
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

    @app.patch("/auth/v1/profile", auth_required=True)
    async def update_profile(request):
        return {"status": "ok"}