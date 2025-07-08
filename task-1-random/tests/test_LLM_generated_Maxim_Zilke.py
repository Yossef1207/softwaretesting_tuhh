import pytest
from hypothesis import given, strategies as st
import sys
from streamlink.options import Options


#class TestClass:
#    @staticmethod
#    def _normalize_key(name: str) -> str:
#        return name.replace("_", "-")


class TestNormalizeKey:
    
    @given(st.text())
    def test_normalize_key_returns_string(self, name):
        """Test that _normalize_key always returns a string regardless of input."""
        result = Options._normalize_key(name)
        assert isinstance(result, str)
    
    @given(st.text(alphabet=st.characters(blacklist_categories=('Cc', 'Cs'))))
    def test_normalize_key_no_underscores_in_output(self, name):
        """Test that the output never contains underscores."""
        result = Options._normalize_key(name)
        assert "_" not in result
    
    @given(st.text())
    def test_normalize_key_preserves_length_or_reduces(self, name):
        """Test that normalization doesn't increase string length."""
        result = Options._normalize_key(name)
        # Length should be preserved (underscores replaced 1:1 with hyphens)
        assert len(result) == len(name)
    
    @given(st.text(alphabet=st.characters(min_codepoint=32, max_codepoint=126)))
    def test_normalize_key_underscore_count_equals_hyphen_increase(self, name):
        """Test that the number of underscores in input equals the increase in hyphens in output."""
        original_hyphen_count = name.count("-")
        original_underscore_count = name.count("_")
        
        result = Options._normalize_key(name)
        result_hyphen_count = result.count("-")
        
        # The increase in hyphens should equal the original underscore count
        hyphen_increase = result_hyphen_count - original_hyphen_count
        assert hyphen_increase == original_underscore_count


# Additional specific test cases for edge cases
class TestNormalizeKeySpecific:
    
    def test_empty_string(self):
        """Test with empty string."""
        assert Options._normalize_key("") == ""
    
    def test_no_underscores(self):
        """Test string without underscores remains unchanged."""
        assert Options._normalize_key("hello-world") == "hello-world"
    
    def test_only_underscores(self):
        """Test string with only underscores."""
        assert Options._normalize_key("___") == "---"
    
    def test_mixed_underscores_and_hyphens(self):
        """Test string with both underscores and hyphens."""
        assert Options._normalize_key("hello_world-test_case") == "hello-world-test-case"