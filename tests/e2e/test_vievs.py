# from warehouse_ddd_alexandra import flask_app

def test_admin_dashboard(test_app):
    test_client = test_app.test_cliernt()
    response = test_client.get('/admin')

    assert b"Dashboard" in response
    assert b'<tr class="border-b border-dashed last:border-b-0">' in response

def test_admin_batches_get(test_app):
    test_client = test_app.test_cliernt()
    response = test_client.get("/admin/batches")

    assert b"Batches" in response

def test_admin_batches_post(test_app):
    test_client = test_app.test_cliernt()
    response = test_client.get("/admin/batches", data={
        "reference": "batch-test",
        "sku": "table-test",
        "qty": 10,
        "eta": None
    })

    assert b"Batches" in response
    assert b"batch-test" in response
    assert b"table-test" in response
    assert b"10" in response
    
def test_auth_login_get(test_app):
    test_client = test_app.test_client()
    response = test_client.get("/auth/login")

    assert b"Login" in response

def test_auth_login_success_for_existing_user(test_app):
    test_client = test_app.test_client(follow_redirects=True)
    response = test_client.get("/auth/login", data={
        "email": "test@gmail.com",
        "password": "testpassword"
    })
    assert response.request.path == "/admin"


def test_auth_login_error_for_unknown_user(test_app):
    test_client = test_app.test_client()
    response = test_client.post(
        "/auth/login",
        data={"email": "unknown@gmail.com", "password": "testpassword"},
    )
    assert b'Invalid login or password. Try again' in response

