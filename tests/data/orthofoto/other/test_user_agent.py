from src.data.orthofoto.other.user_agent import UserAgent


def test_user_agent_random():
    user_agent = UserAgent()
    assert len(user_agent.random) > 0
