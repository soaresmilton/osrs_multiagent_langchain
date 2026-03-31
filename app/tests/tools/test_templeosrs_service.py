from app.tools.templeosrs.service import TempleOsrsService

def test_get_player_stats_success(mocker):

    mock_client = mocker.Mock()
    mock_client.get_player_stats.return_value = {"Overall_level": 2376}

    service =  TempleOsrsService(client=mock_client)

    result = service.get_player_stats(username="Hoom Pk", date=1774959558)

    assert result.success is True
    assert result.data["Overall_level"] == 2376

    mock_client.get_player_stats.assert_called_once_with(
        username="Hoom Pk",
        date=1774959558
    )

def test_get_player_stats_exception(mocker):
    mock_client = mocker.Mock()
    mock_client.get_player_stats.side_effect = Exception("API error")

    service = TempleOsrsService(client=mock_client)
    result = service.get_player_stats("Hoom Pk", 1774959558)

    assert result.success is False
    assert "Failed to fetch player stats" in result.error

def test_get_player_stats_empty_response(mocker):
    mock_client = mocker.Mock()
    mock_client.get_player_stats.return_value = None

    service = TempleOsrsService(client=mock_client)

    result = service.get_player_stats("Hoom Pk", 1774959558)

    assert result.success is False
    assert result.error == "Empty response from API"

def test_get_player_info(mocker):
    mock_client = mocker.Mock()
    mock_client.test_get_player_info.return_value = {"Username": "Hoom Pk"}

    service = TempleOsrsService(client=mock_client)

    result = service.get_player_info("Hoom Pk")

    assert result.success is True
    assert result.data['Username'] == "Hoom Pk"