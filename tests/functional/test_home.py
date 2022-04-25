def test_index_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_route(app, client):
     with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200


def test_add_friend_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200

def test_age_future_functionality(app, client):
    print("-- /result 'estimate_total' POST test")
    with app.test_client() as test_client:
        cost = {"radius":"180", "height":"360"} 
        res = test_client.post('/estimate', data=cost)
        assert res.status_code == 200
        assert b"141,300"