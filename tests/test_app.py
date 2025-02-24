# tests/test_app.py
import pytest
from app import SnippetManager

@pytest.fixture
def snippet_manager():
    """Fixture to create a new instance of SnippetManager for each test."""
    return SnippetManager()

def test_save_and_list_snippets(snippet_manager):
    # Initially, the snippet list should be empty
    assert len(snippet_manager.list_snippets()) == 0
    
    # Save a new snippet and check that it's added
    snippet_id = snippet_manager.save_snippet("python", "Example snippet", "print('Hello')")
    assert snippet_id is not None
    
    snippets = snippet_manager.list_snippets()
    assert len(snippets) == 1
    # Validate snippet content
    snippet = snippets[0]
    assert snippet["language"] == "python"
    assert snippet["description"] == "Example snippet"
    assert snippet["code"] == "print('Hello')"

def test_view_snippet(snippet_manager):
    # Save a snippet and retrieve it
    snippet_id = snippet_manager.save_snippet("python", "Test snippet", "print('test')")
    snippet = snippet_manager.view_snippet(snippet_id)
    assert snippet["language"] == "python"
    assert snippet["description"] == "Test snippet"
    assert snippet["code"] == "print('test')"

def test_delete_snippet(snippet_manager):
    # Save and then delete a snippet, verifying that it no longer exists
    snippet_id = snippet_manager.save_snippet("python", "Delete snippet", "print('delete')")
    result = snippet_manager.delete_snippet(snippet_id)
    assert result is True
    with pytest.raises(KeyError):
        # Attempting to view a deleted snippet should raise an error
        snippet_manager.view_snippet(snippet_id)

def test_edit_snippet(snippet_manager):
    # Save a snippet, then update its content
    snippet_id = snippet_manager.save_snippet("python", "Edit snippet", "print('old')")
    result = snippet_manager.edit_snippet(snippet_id, {"code": "print('new')"})
    assert result is True
    snippet = snippet_manager.view_snippet(snippet_id)
    assert snippet["code"] == "print('new')"

def test_find_snippet(snippet_manager):
    # Save multiple snippets and then search by keyword
    snippet_manager.save_snippet("python", "Sort algorithm", "def sort(): pass")
    snippet_manager.save_snippet("javascript", "Event handler", "function handle() {}")
    results = snippet_manager.find_snippet("sort")
    assert len(results) == 1
    assert results[0]["description"] == "Sort algorithm"

def test_share_snippet(snippet_manager):
    # Save a snippet and simulate sharing it with a user/group
    snippet_id = snippet_manager.save_snippet("python", "Share snippet", "print('share')")
    result = snippet_manager.share_snippet(snippet_id, "user123")
    assert result is True
