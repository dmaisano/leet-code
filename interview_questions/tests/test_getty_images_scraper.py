from unittest.mock import AsyncMock
import pytest
from playwright.async_api import BrowserContext
from pytest_mock import MockerFixture

from interview_questions.getty_images_scraper import (
    fetch_images_from_page,
    search_getty_images,
)


@pytest.mark.asyncio
async def test_fetch_images_from_page(mocker: MockerFixture) -> None:
    # Mocking a BrowserContext and a page
    mock_context = mocker.Mock(spec=BrowserContext)
    mock_page = mocker.AsyncMock()

    # Mocking the page creation and navigation
    mock_context.new_page.return_value = mock_page
    mock_page.goto.return_value = None

    # Mocking the image elements on the page
    mock_img_element = mocker.Mock()
    mock_img_element.get_attribute = AsyncMock(
        return_value="https://example.com/image.jpg"
    )

    # Mocking the query selector to return the mocked image element
    mock_page.query_selector_all.return_value = [mock_img_element]

    # Calling the function
    result = await fetch_images_from_page(mock_context, "https://example.com/search", 1)

    # Assertions
    assert result == ["https://example.com/image.jpg"]
    mock_page.goto.assert_called_once_with("https://example.com/search?page=1")
    mock_page.query_selector_all.assert_called_once_with("a > figure > picture > img")
    mock_img_element.get_attribute.assert_called_with("src")


@pytest.mark.asyncio
async def test_search_getty_images(mocker: MockerFixture) -> None:
    # Mocking the fetch_images_from_page to return a list of image URLs
    mock_fetch = mocker.patch(
        "interview_questions.getty_images_scraper.fetch_images_from_page",
        return_value=["https://example.com/image.jpg"],
    )

    # Call the function
    result = await search_getty_images("test search", 1)

    # Assertions
    assert result == ["https://example.com/image.jpg"]
    mock_fetch.assert_called_once_with(
        mocker.ANY, "https://www.gettyimages.com/photos/test-search", 1
    )


if __name__ == "__main__":
    pytest.main()
