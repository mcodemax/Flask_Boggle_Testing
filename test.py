from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_generate_board(self):
        """
            test if board being generated correctly
        """
        with self.client as client: #ver of server that we can use in testing
            res = client.get('/') # sends the request
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn('<div id="score">CURRENT SCORE:0</div>', html)

            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('plays'))



    #https://stackoverflow.com/questions/43104688/accessing-session-object-during-unit-test-of-flask-application        

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check_word?word=cat')
        self.assertEqual(response.json['result'], 'ok')


    def test_invalid_word(self):
        """Test if word is in game"""

        self.client.get('/')
        response = self.client.get('/check_word?word=appreciatingly')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_non_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get('/check_word?word=okksf')
        self.assertEqual(response.json['result'], 'not-word')




    #tests below to refactor and add later



    # def test_updatescores_redirect(self):
    #     """make sure we redirect to the correct place"""

    #     res = self.client.post('/update_score_plays')

    #     self.assertEqual(res.status_code, 302)


        
    # def test_get_user_guess(self):
    #     """
    #         test the backend and make sure we get the user's word from html
    #     """
    
    #     with self.client as client:
    #         res = client.post("/update_score_plays", data={'guess':'baby'})
    #         html = res.get_data(as_text=True)

    #         rv = client.post('/update_score_plays', json={
    #             'email': 'flask@example.com', 'password': 'secret'
    #         })
    #         json_data = rv.get_json()
    #         assert verify_token(email, json_data['token'])

    #         with client.session_transaction() as sess: